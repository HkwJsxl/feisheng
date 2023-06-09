import http from "../utils/http";
import {reactive, ref} from "vue"


const course = reactive({
    current_direction: 0,  // 当前选中的学习方向，0表示所有方向
    current_category: 0,  // 当前选中的课程分类，0表示不限分类
    direction_list: [],    // 学习方向列表
    category_list: [],    // 课程分类列表
    course_list: [],       // 课程列表数据
    ordering: "-id",       // 课程排序条件
    page: 1,               // 当前页码，默认为1
    size: 5,               // 当前页数据量
    count: 0,         // 课程信息列表的数量
    has_perv: false,  // 是否有上一页
    has_next: false,  // 是否有下一页
    timer: null,      // 课程相关数据的定时器
    text: "",         // 搜索文本框内容
    hot_word_list: [],// 热搜词列表
    course_id: null,  // 课程ID
    info: {           // 课程详情信息
        teacher: {},   // 课程相关的老师信息
        discount: {    // 课程相关的折扣信息
            type: ""
        }
    },
    tabIndex: 1,      // 课程详情页中默认展示的课程信息的选项卡
    chapter_list: [], // 课程章节列表

    course_type: [],  // 我的课程-课程类型列表
    current_course_type: -1,  // 我的课程-当前显示的课程类型，默认为-1，表示全部
    user_course_count: 0,    // 我的课程-课程列表总数
    user_course_list: [], // 用户中心的课程列表

    lesson_list: [],
    lesson_tree_props: {
        children: 'children',
        label: 'label',
    },
    user_course: {},       // 用户在当前课程的学习进度记录
    current_chapter: null, // 正在学习的章节ID
    current_lesson: null,  // 正在学习的课时ID
    lesson_link: null,  // 正在学习的课时视频ID
    player: null,       // 当前页面的视频播放器对象
    current_time: 0,    // 播放器，当前播放时间
    course_info: [],    // 课程信息

    get_course_direction() {
        // 获取学习方向信息
        return http.get("/course/direction/")
    },
    get_course_category() {
        // 获取课程分类信息
        if (this.current_direction === 0) {
            return http.get('/course/category/')
        } else {
            return http.get(`/course/category/?direction=${this.current_direction}`)
        }
    },
    get_course_list() {
        let params = {
            page: this.page,
            size: this.size,
        }
        if (this.ordering) {
            params.ordering = this.ordering;
        }
        // 方向和分类都为全部时获取全部的课程列表
        if (this.current_direction === 0 && this.current_category === 0) {
            return http.get(`/course/`, {
                params
            })
        }
        // 方向未动，直接点击分类时发出请求
        if (this.current_direction === 0 && this.current_category !== 0) {
            return http.get(`/course/?category=${this.current_category}`, {
                params
            })
        }
        // 分类为全部时发出请求
        if (this.current_category === 0) {
            return http.get(`/course/?direction=${this.current_direction}`, {
                params
            })
        }
        // 获取课程列表信息
        return http.get(`/course/?direction=${this.current_direction}&category=${this.current_category}`, {
            params
        })
    },
    start_timer() {
        // 课程相关的优惠活动倒计时
        clearInterval(this.timer); // 保证整个页面只有一个倒计时对优惠活动的倒计时进行时间
        this.timer = setInterval(() => {
            this.course_list.forEach((course) => {
                // js的对象和python里面的字典/列表一样， 是属于引用类型的。所以修改了成员的值也会影响自身的。
                if (course.discount.expire && course.discount.expire > 0) {
                    // 时间不断自减
                    course.discount.expire--
                }
            })
        }, 1000)
    },
    search_course() {
        // 课程搜索
        let params = {
            page: this.page,
            size: this.size,
            text: this.text,
        }
        if (this.ordering) {
            params['ordering'] = this.ordering
        }
        return http.get(`/course/search/`, {
            params,
        })
    },
    get_hot_word() {
        // 课程热搜关键字
        return http.get("/course/search/hot/")
    },
    get_course() {
        return http.get(`/course/${this.course_id}/`)
    },
    get_course_chapters() {
        // 获取指定课程的章节列表
        return http.get(`/course/${this.course_id}/chapter/`)
    },
    get_course_type_list(token) {
        // 获取课程类型
        return http.get("/course/type/")
    },
    get_user_course_list(token) {
        // 获取用户的课程列表
        return http.get("/user/course/", {
            params: {
                type: this.current_course_type,
                page: this.page,
                size: this.size,
            },
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
    get_user_course(token) {
        // 获取用户的指定课程信息包含学习进度
        return http.get(`/user/course/${this.course_id}/`, {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
    get_lesson_study_time(lesson, token) {
        // 获取课程课时学习进度时间
        return http.get("/user/lesson/", {
            params: {
                lesson,
            },
            headers: {
                Authorization: "jwt " + token,
            }
        })
    },
    update_user_study_progress(lesson, seed, token) {
        // 更新课时学习的进度
        return http.post('/user/progress/', {
            time: seed,
            lesson: lesson,
        }, {
            headers: {
                Authorization: "jwt " + token,
            }
        })
    }
})

export default course;
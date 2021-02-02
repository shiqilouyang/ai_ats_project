create database test;
use test;

CREATE TABLE IF NOT EXISTS `ale_result_record_9` (
  `rid` bigint(20)  NOT NULL  auto_increment COMMENT  '自增id',
  `session_id` varchar(32) NOT NULL COMMENT '会话编号 主键非自增，程序生成',
  `user_id` varchar(32) NOT NULL DEFAULT '' COMMENT '用户ID',
  `class_id` varchar(32) NOT NULL DEFAULT '' COMMENT '班级ID',
  `course_id` varchar(32) NOT NULL DEFAULT '' COMMENT '课程ID',
  `section_id` varchar(32) NOT NULL DEFAULT '' COMMENT '阶段ID',
  `env` varchar(32) NOT NULL DEFAULT '' COMMENT '环境ID',
  `itemId` varchar(32) NOT NULL DEFAULT '' COMMENT 'item ID',
  `user_name` varchar(32) NOT NULL DEFAULT '' COMMENT '阶段ID',
  `activityType`  varchar(32) NOT NULL DEFAULT '' COMMENT '行为类型',
  `usage`  varchar(32) NOT NULL DEFAULT '' COMMENT '题目用途',
  `loCode` varchar(32) NOT NULL DEFAULT '' COMMENT '知识点code',
  `ability` float NOT NULL COMMENT '知识点能力值',
  `initability` float NOT NULL COMMENT '初始知识点能力值',
  `curPoolCode` varchar(32) NOT NULL DEFAULT '' COMMENT '当前模块',
  `studylonum`  int NOT NULL  COMMENT '学习过知识点数量',
  `prePoolCode`  varchar(32) DEFAULT '' COMMENT '上一个模块',
   `unlockLoNum`  int NOT NULL COMMENT '解锁知识点数量',
   `curlocode`  varchar(32) NOT NULL DEFAULT '' COMMENT '当前知识点',
   `preLoCode`  varchar(32)  DEFAULT '' COMMENT '上一个知识点',
   `starttime` varchar(32) NOT NULL DEFAULT ''  COMMENT '做题开始时间',
   `duration` varchar(32) NOT NULL DEFAULT '' COMMENT '做题时长',
   `score`   varchar(32)  NOT NULL COMMENT '是否正确',
   `rate`   float  NOT NULL COMMENT '正答率',
  PRIMARY KEY (`rid`),
  KEY `user_id` (`user_id`),
  KEY `session_id` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='做题记录表';


CREATE TABLE IF NOT EXISTS `operation_table` (
  `rid` bigint(20)  NOT NULL  auto_increment COMMENT  '自增id',
  `session_id` varchar(32)  COMMENT '会话编号 主键非自增，程序生成',
  `user_id` varchar(32) NOT NULL DEFAULT '' COMMENT '用户ID',
  `class_id` varchar(32)  DEFAULT '' COMMENT '班级ID',
  `course_id` varchar(32)  DEFAULT '' COMMENT '课程ID',
  `section_id` varchar(32)  DEFAULT '' COMMENT '阶段ID',
  `user_name` varchar(32)  DEFAULT '' COMMENT '阶段ID',
  `env` varchar(32)  DEFAULT '' COMMENT '运行环境',
   `starttime` varchar(32)  DEFAULT ''  COMMENT '做题开始时间',
   `rate`   float  COMMENT '正答率',
   `thid` varchar(32)  DEFAULT '' COMMENT '线程Id',
	`message` varchar(32)  DEFAULT '' COMMENT '通信',
	`status` varchar(32)  DEFAULT '' COMMENT '状态',
  PRIMARY KEY (`rid`),
  KEY `user_id` (`user_id`),
  KEY `session_id` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='校验做题记录表';

CREATE TABLE IF NOT EXISTS `operation_table_tester` (
  `rid` bigint(20)  NOT NULL  auto_increment COMMENT  '自增id',
  `session_id` varchar(32)  COMMENT '会话编号 主键非自增，程序生成',
  `user_id` varchar(32) NOT NULL DEFAULT '' COMMENT '用户ID',
  `class_id` varchar(32)  DEFAULT '' COMMENT '班级ID',
  `course_id` varchar(32)  DEFAULT '' COMMENT '课程ID',
  `section_id` varchar(32)  DEFAULT '' COMMENT '阶段ID',
  `user_name` varchar(32)  DEFAULT '' COMMENT '阶段ID',
  `env` varchar(32)  DEFAULT '' COMMENT '运行环境',
   `starttime` varchar(32)  DEFAULT ''  COMMENT '做题开始时间',
   `rate`   float  COMMENT '正答率',
   `thid` varchar(32)  DEFAULT '' COMMENT '线程Id',
	`message` varchar(32)  DEFAULT '' COMMENT '通信',
	`status` varchar(32)  DEFAULT '' COMMENT '状态',
  PRIMARY KEY (`rid`),
  KEY `user_id` (`user_id`),
  KEY `session_id` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='校验做题记录表(测试用户专用)';

--  user_id 为 xfl-46841606022556 的 用户在重学习模块之中每个知识点 做题+视频 的总个数
-- select loCode,COUNT(rid) t,ability  from ale_test_result_record where user_id = "xfl-46841606022556"  and `curPoolCode` = "RESTUDY_MODULE"    group by loCode order by t desc ;

--  user_id 为 xfl-46841606022556 的 用户在重学习模块之中每个知识点的轮数
-- select loCode,COUNT(rid) t,ability  from ale_test_result_record where user_id = "xfl-46841606037306" and `usage` = "LO"  and `curPoolCode` = "RESTUDY_MODULE"    group by loCode order by t desc ;

CREATE TABLE `exercese_rule`  (
  `rid` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `testmodeRule` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `studymodeRule` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `restudymodeRule` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `academicSeason_subject` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '学段与学科',
  `testModeNum` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '测试模块做题数量',
  `studyModeNum` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学习模块做题数量',
  `restudyModeNum` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '重学习模块做题数量',
  `test_ability` float NULL DEFAULT NULL COMMENT '测试知识点能力值',
  `study_ability` float NULL DEFAULT NULL COMMENT '学习知识点能力值',
  `restudy_ability` float NULL DEFAULT NULL COMMENT '重学习知识点能力值',
  `test_exerceseTime` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '测试做题时长',
  `study_exerceseTime` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学习做题时长',
  `restudy_exerceseTime` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '重学习做题时长',
  `rule_groupId` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`rid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '做题规则表' ROW_FORMAT = Dynamic;

-- INSERT INTO `exercese_rule` VALUES (1, '第一题对，算掌握。第一题错，算未掌握', '● 视频：1个● 互动题：最多1道（没有则跳过）● 混合推题：3道（学+测【优先学习题】）● 高中做完2题后判定能力值是否达标，能力值>=0.7，最多做3题如果此时仍然没达标，则将知识点放回重学隔离池。', '● 视频&讲义：1道● 混合推题（学+测）：2道● 重学模块1轮2道题，第一道错了切换知识点，两道连对算达标，其余情况算未达标。', '高中数学常规', '1', 'mv_1_mix_3_iv_1', 'mv_1_mix_2', 0.7, 0.7, 0.7, '900', '900', '900', '21401');
-- INSERT INTO `exercese_rule` VALUES (classes, '● 无测试模块', '● 推题规则 ● 视频&讲义：1道  ● 混合推题（学+测）：classes-5道  ● 达标规则调整 ○ 做完2题后判定能力值是否达标（达标条件：能力值>=0.7），之后每做一道题判定一次，最多做5题', '● 无重学习模块', '数学冲刺章', '0', 'mv_0_mix_5_iv_0', 'mv_0_mix_0', 0, 0.7, 0, '0', '0', '0', '20304');
-- INSERT INTO `exercese_rule` VALUES (3, '● 第一题对，算掌握。第一题错，算未掌握', '● 视频：1个● 互动题：最多1道（没有则跳过）● 混合推题：5道（学+测【优先学习题】）●初中做完2题后判定能力值是否达标，学种&学苗&学中& 学霸能力值>=0.7，最多做5-8题如果此时仍然没达标，则将知识点放回重学隔离池', '● 视频&讲义：1道● 混合推题（学+测）：5道	○ 从第二题开始判断，能力值>=0.7算达标。○ 以下情况知识点立刻判定重学放弃，进入顽固知识点隔离池 ■ 前两道正答率=0% ■ 做五道题能力值依然低于0.7', '初中数学常规章', '1', 'mv_1_mix_8_iv_1_ex_3', 'mv_1_mix_15', 0.7, 0.7, 0.7, '600', '600', '600', '20401');
-- INSERT INTO `exercese_rule` VALUES (4, '● 第一题错误，退出，算未掌握● 第一题正确，做第二题，两题都对算掌握', '● 视频：1个● 互动题：最多1道（没有则跳过）● 混合推题：5道（学+测【优先学习题】）●小学做完3题后判定能力值是否达标，学种&学苗&学中& 学霸能力值>=0.7，最多做5-8题如果此时仍然没达标，则将知识点放回重学隔离池。', '● 视频&讲义：1道● 混合推题（学+测）：5道	○ 从第二题开始判断，能力值>=0.7算达标。○ 以下情况知识点立刻判定重学放弃，进入顽固知识点隔离池 ■ 前两道正答率=0% ■ 做五道题能力值依然低于0.7', '小学数学常规章', 'classes', 'mv_1_mix_8_iv_1_ex_3', 'mv_1_mix_15', 0.7, 0.7, 0.7, '600', '600', '600', '22401');
-- INSERT INTO `exercese_rule` VALUES (5, '● 2道练习题 ● 第一题错误，退出，算未掌握 ● 第一题正确，做第二题，两题都对算掌握 ● 第一题正确，第二题错误算未掌握', '● 基础知识点○ 视频：1个○ 互动题：最多1道（没有则跳过）○ 混合推题：4道（学+测）● 综合知识点○ 视频：1个○ 互动题：最多1道（没有则跳过）○ 混合推题：3道（学+测）● 混合推题：4道（学+测）● 做完3题后开始判定能力值>=0.7达标；最多做完4题就退出', '● 视频：1道● 混合推题（学+测）：4道● 每4题后依然未达标，则会放回重学隔离池，下一轮重学能力值重新初始化 做完3题后判定能力值是否达标，学种&学苗&学中& 学霸能力值>=0.7', '物理人教版', 'classes', 'mv_1_mix_8_iv_2', 'mv_1_mix_4', 0.7, 0.7, 0.7, '900', '900', '900', '40301');


CREATE TABLE IF NOT EXISTS `old_user`(
      `rid` bigint(20)  NOT NULL  auto_increment COMMENT  '自增id',
       `date` varchar(32)  NOT NULL COMMENT '用户创建时间',
       `user_id` varchar(32) NOT NULL DEFAULT '' COMMENT '用户ID',
        PRIMARY KEY (`rid`),
        KEY `user_id` (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='老用户表';

-- LOAD DATA LOCAL INFILE 'D:\\test1.txt' INTO TABLE old_user;

CREATE TABLE IF NOT EXISTS `rule_activity_test_result_record`(
     `rid` bigint(20) NOT NULL auto_increment COMMENT '自增id',
     `user_id` varchar(32) NOT NULL DEFAULT '' COMMENT '用户ID',
     `course_id` varchar(32) NOT NULL DEFAULT '' COMMENT '课程ID',
     `class_id` varchar(32) NOT NULL DEFAULT '' COMMENT '班级ID',
     `section_id` varchar(32) NOT NULL DEFAULT '' COMMENT '阶段ID',
      `academicSeason_subject` varchar(32) NOT NULL  COMMENT '学段与学科',
     `message` TEXT not null COMMENT '结果信息',
     `testMode_maxNum`  varchar(32)  COMMENT '测试模块实际最大做题数量',
     `studyMod_maxNum`  varchar(32)  COMMENT '学习模块实际最大做题数量',
     `restudyMode_maxNum`  varchar(32)  COMMENT '重学习模块实际最大做题数量',
     `testMode_minNum`  varchar(32)  COMMENT '测试模块实际最小做题数量',
     `studyMod_minNum`  varchar(32)  COMMENT '学习模块实际最小做题数量',
     `restudyMode_minNum`  varchar(32)  COMMENT '重学习模块实际最小做题数量',
     `is_success` int not null COMMENT '测试行为是否成功',
     `test_Time` varchar(32) not null COMMENT '测试时间',
      PRIMARY KEY (`rid`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='测试行为结果表';
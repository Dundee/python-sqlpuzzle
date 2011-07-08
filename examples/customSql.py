#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sqlpuzzle
# Michal Horejsek <horejsekmichal@gmail.com>
# https://github.com/horejsek/sqlpuzzle
#

import sqlpuzzle
import sqlpuzzle.customSql


avg = sqlpuzzle.customSql.CustomSql('AVG(`age`) AS "avgAge"')
table = sqlpuzzle.customSql.CustomSql('`user` LEFT JOIN `country` ON `user`.`country_id`=`country`.`id`')
where = sqlpuzzle.customSql.CustomSql('(`enable` = 1 OR `vip` = 1)')

sql = sqlpuzzle.select('country.name', avg).from_(table)
sql.where(where).where(planet='Earth')
sql.groupBy('user.country_id')

print sql
#
# output:
# (for better reading splited to more lines)
#
# SELECT `country`.`name`, AVG(`age`) AS "avgAge"
# FROM `user` LEFT JOIN `country` ON `user`.`country_id`=`country`.`id`
# WHERE (`enable` = 1 OR `vip` = 1) AND `planet` = "Earth"
# GROUP BY `user`.`country_id`
#


table = sqlpuzzle.customSql.CustomSql('`user`')
set_ = sqlpuzzle.customSql.CustomSql('`age` = `age` + 1')

sql = sqlpuzzle.update(table).set(set_).where(where)
print sql
# output:
# UPDATE `user` SET `age` = `age` + 1 WHERE (`enable` = 1 OR `vip` = 1)


print sqlpuzzle.deleteFrom(table).where(where)
# output:
# DELETE FROM `user` WHERE (`enable` = 1 OR `vip` = 1)


print sqlpuzzle.insertInto(table).values(name='Alan')
# output:
# INSERT INTO `user` (`name`) VALUES ("Alan")

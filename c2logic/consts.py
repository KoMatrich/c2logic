# see https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/logic/LogicOp.java
import operator

binary_ops = {
	"+": "add",
	"-": "sub",
	"*": "mul",
	"/": "div",
	"%": "mod",
	"==": "equal",
	"!=": "notEqual",
	"<": "lessThan",
	"<=": "lessThanEq",
	">": "greaterThan",
	">=": "greaterThanEq",
	">>": "shr",
	"<<": "shl",
	"|": "or",
	"&": "and",
	"^": "xor"
}
binary_ops_python = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.floordiv,
	"%": operator.mod,
	"==": operator.eq,
	"!=": operator.ne,
	"<": operator.lt,
	"<=": operator.le,
	">": operator.gt,
	">=": operator.ge,
	">>": operator.rshift,
	"<<": operator.lshift,
	"|": operator.or_,
	"&": operator.and_,
	"^": operator.xor,
}
condition_ops = {
	"==": "equal",
	"!=": "notEqual",
	"<": "lessThan",
	"<=": "lessThanEq",
	">": "greaterThan",
	">=": "greaterThanEq"
}
unary_ops = {"~": "not"}
unary_ops_python = {"~" : operator.invert}

binary_op_inverses = {"==": "!=", "!=": "==", "<": ">=", "<=": ">", ">": "<=", ">=": "<"}

func_binary_ops = ["pow", "max", "min", "angle", "len", "land", "idiv", "strictEqual", "noise"]
func_unary_ops = ["abs", "log", "log10", "sin", "cos", "tan", "floor", "ceil", "sqrt", "rand"]
binary_ops.update(dict(zip(func_binary_ops, func_binary_ops)))
unary_ops.update(dict(zip(func_unary_ops, func_unary_ops)))
SPECIAL_VARS = (
	'counter', 'ipt', 'links', 'maph', 'mapw', 'this', 'thisx', 'thisy', 'tick', 'time', 'unit'
)

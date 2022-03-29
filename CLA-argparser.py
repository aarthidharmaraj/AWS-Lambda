import argparse

if __name__=='__main__':
    ##Initialize the parser
    parser=argparse.ArgumentParser(
        description="Arithmetic operation"
    )
    
    # parser.add_argument('num1',help='Number 1',type=float)
    # parser.add_argument('num2',help='Number 2',type=float)
    # parser.add_argument('operation',help='Provide operation')
    ##irrespective of position when passed by providing a default operator
    # parser.add_argument('--num1',help='Number 1',type=float)
    # parser.add_argument('--num2',help='Number 2',type=float)
    # parser.add_argument('--operation',help='Provide operation',default='+')
    ##by providing a short key for them
    parser.add_argument('-n','--num1',help='Number 1',type=float)
    parser.add_argument('-p','--num2',help='Number 2',type=float)
    parser.add_argument('-o','--operation',help='Provide operation')
    args=parser.parse_args()
    print(args)
    
    result=0
    if args.operation=='+':
        result=args.num1+args.num2
    if args.operation=='-':
        result=args.num1-args.num2
    if args.operation=='*':
        result=args.num1*args.num2
    if args.operation=='pow':
        result=pow(args.num1,args.num2)
    
    print("The result of the operation is", round(result))
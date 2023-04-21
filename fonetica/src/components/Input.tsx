interface Props {
    Label: string;
    forLabel: string;
    type: string;
    placeholder?: string;
}

export default function Input({Label, forLabel, type, placeholder }: Props) {
    return(
        <div className="flex flex-col mb-6 items-center">
            <label htmlFor={forLabel} 
                className="w-3/4 px-1 text-left mb-2 text-sm font-medium text-gray-900">
                {Label}
            </label>
            <input type={type} id={forLabel} 
                className="flex bg-white border border-gray-300 
                    text-gray-900 text-sm rounded-lg 
                    focus:ring-blue-500 focus:border-blue-500 
                    w-3/4 p-2.5 text-left"
                    placeholder={placeholder} required />
        </div>
    )
}
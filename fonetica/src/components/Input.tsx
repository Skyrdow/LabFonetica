import React from "react";

interface Props {
    Label: string;
    forLabel: string;
    type: string;
    placeholder?: string;
}

export default function Input({Label, forLabel, type, placeholder }: Props) {
    return(
        <div className="flex flex-col mb-4 text-left font-usach-helvetica-medium">
            <input type={type} id={forLabel} 
                className="flex bg-white border border-gray-100 
                     text-usach-industrial-1000 text-sm rounded-lg 
                    focus:ring-usach-terra-800 focus:border-usach-terra-800
                    w-full p-2.5 text-left font-usach-helvetica-body"
                    placeholder={placeholder} required />
        </div>
    )
}
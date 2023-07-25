import React from "react";

interface Props {
    href?: string;
    label: string;
    type?: string;
}
  
export default function Boton({ label, href, type }: Props) {
    return (
        <button id="boton-pog" className="rounded-lg bg-usach-terra-700 hover:bg-usach-terra-800 text-lg text-white my-2 drop-shadow p-2" itemType={type}>
            <a className="font-usach-helvetica-medium px-max" href={href}>{label}</a>
        </button>
    );
}
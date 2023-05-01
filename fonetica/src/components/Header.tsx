import React from "react";

export default function Header() {
    return (
        <header className="bg-usach-aqua-900 p-2 gap-10 flex h-48">
            <button className="w-1/3">
                <a href="/" className="">
                    <img src="/Usach SB.png" alt="Logo Usach" className=" w-full h-full object-contain"/>
                </a>
            </button>
            <h1 className="m-auto text-5xl font-usach-bebas-title text-white align-middle">Recursos Virtuales para el aprendizaje del Lenguaje</h1>
        </header>
    )
}
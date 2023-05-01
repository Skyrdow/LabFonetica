import React from "react";

interface Props {
    label: string;
    image: string;
}
  
export default function Juego({ label, image }: Props) {
    return (
        <div className="flex-col px-20 justify-center text-center text-white">
            <h1 className="pt-6 pb-4 text-5xl font-usach-bebas-title">{label}</h1>
            <div className="flex flex-col h-64 mb-5">
                <img src={image} className="m-auto w-full h-full object-contain"/>
            </div>
            <p className=" text-xl  font-usach-bebas-body my-2 ">En este juego debes contar la cantidad de sílabas que tiene cada palabra y seleccionar la respuesta correcta.</p>
            <div className="my-6">
                <button className="rounded-lg bg-usach-rouge-800 h-full">
                    <a className="text-5xl font-usach-bebas-title mx-7" href="#">JUGAR</a>
                </button>
            </div>
        </div>
    );
}
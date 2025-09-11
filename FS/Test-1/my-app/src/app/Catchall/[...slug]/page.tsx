export default async function Catchall ({params,}: {params : Promise <{slug: string[]}>}){
    
    const {slug} = await params;
    if (slug?.length === 2){
        return (<>
        <h1>Viewing docs for feature  {slug[0]}  and concept {slug[1]} </h1></>)
    }
    else if(slug?.length === 1){
        return (
            <>
            <h1>Viewing docs</h1></>
        )
    }
    else {
        return (<>
        <h1>Doc Home Page</h1></>)
    }
}

import React from 'react';

const Results = ({ recommendations, onReset }) => {
    if (!recommendations || recommendations.length === 0) {
        return (
            <div className="text-center p-8">
                <p className="text-gray-600">No recommendations found based on your profile.</p>
                <button onClick={onReset} className="mt-4 text-primary hover:underline">Try Again</button>
            </div>
        );
    }

    return (
        <div className="max-w-4xl mx-auto">
            <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold text-gray-800">Recommended Funds</h2>
                <button
                    onClick={onReset}
                    className="text-sm text-gray-600 hover:text-primary border border-gray-300 px-4 py-2 rounded-lg hover:bg-gray-50 transition-colors"
                >
                    Start Over
                </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {recommendations.map((fund, index) => (
                    <div key={index} className="bg-white rounded-xl shadow-lg overflow-hidden border border-gray-100 hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 animate-fade-in-up" style={{ animationDelay: `${index * 100}ms` }}>
                        <div className="p-6">
                            <div className="flex justify-between items-start mb-4">
                                <div>
                                    <h3 className="text-lg font-bold text-gray-900 mb-1 leading-tight">{fund.scheme_name}</h3>
                                    <div className="flex items-center space-x-2 mt-2">
                                        <span className={`inline-block px-3 py-1 text-xs font-semibold rounded-full 
                      ${fund.category === 'Equity' ? 'bg-blue-100 text-blue-800' :
                                                fund.category === 'Debt' ? 'bg-green-100 text-green-800' : 'bg-purple-100 text-purple-800'}`}>
                                            {fund.category}
                                        </span>
                                        <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded-full">{fund.sub_category}</span>
                                    </div>
                                </div>
                                <div className="text-right">
                                    <span className={`block text-sm font-bold 
                    ${fund.risk_level >= 5 ? 'text-red-600' :
                                            fund.risk_level <= 2 ? 'text-green-600' : 'text-yellow-600'}`}>
                                        Risk: {fund.risk_level}/6
                                    </span>
                                </div>
                            </div>

                            <div className="mb-4">
                                <p className="text-sm text-gray-600"><span className="font-semibold">Fund Manager:</span> {fund.fund_manager}</p>
                            </div>

                            <div className="grid grid-cols-3 gap-4 mb-4 bg-gray-50 p-4 rounded-xl">
                                <div className="text-center">
                                    <p className="text-xs text-gray-500 mb-1">1Y Return</p>
                                    <p className={`font-bold ${fund.returns_1yr >= 0 ? 'text-green-600' : 'text-red-600'}`}>{fund.returns_1yr}%</p>
                                </div>
                                <div className="text-center">
                                    <p className="text-xs text-gray-500 mb-1">3Y Return</p>
                                    <p className={`font-bold ${fund.returns_3yr >= 0 ? 'text-green-600' : 'text-red-600'}`}>{fund.returns_3yr}%</p>
                                </div>
                                <div className="text-center">
                                    <p className="text-xs text-gray-500 mb-1">5Y Return</p>
                                    <p className={`font-bold ${fund.returns_5yr >= 0 ? 'text-green-600' : 'text-red-600'}`}>{fund.returns_5yr}%</p>
                                </div>
                            </div>

                            <div className="border-t pt-4">
                                <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Risk Ratios</h4>
                                <div className="grid grid-cols-3 gap-2 text-sm">
                                    <div>
                                        <span className="text-gray-500">Std Dev:</span> <span className="font-medium">{fund.sd}</span>
                                    </div>
                                    <div>
                                        <span className="text-gray-500">Beta:</span> <span className="font-medium">{fund.beta}</span>
                                    </div>
                                    <div>
                                        <span className="text-gray-500">Sharpe:</span> <span className="font-medium">{fund.sharpe}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Results;

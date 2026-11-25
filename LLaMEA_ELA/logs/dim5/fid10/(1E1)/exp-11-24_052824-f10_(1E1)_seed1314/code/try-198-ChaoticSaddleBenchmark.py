import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced polynomial terms with higher degrees and modified coefficients
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**8 + 4*x[i]**6 + 7*x[i]**4 + 3*x[i]**2) * np.sin(0.7 * x[i])
            
        # Intensified sinusoidal component with multiple phase modulations
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Stronger chaotic interaction between dimensions using modified logistic map behavior
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling range
                chaotic_interaction += np.sin(1.5 * x[i] * x[j]) * np.cos(0.6 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Enhanced saddle-point component with additional exponential terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.3 * x[i]**2) + 0.5 * (x[i]**4 - 1) * np.exp(-0.2 * x[i]**2)
            
        # Novel high-order polynomial coupling with complex sinusoidal modulation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.5 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Introduce multiple local minima with varying depths and positions
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(8 * x[i]) * np.cos(3 * x[i]) + 0.8 * np.sin(15 * x[i]) + 0.3 * np.sin(25 * x[i])
            
        # Add novel cross-dimensional coupling with chaotic behavior
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x[i] + x[j]) * np.cos(0.3 * x[i] * x[j]) * (1 + 0.25 * np.sin(2 * (x[i]**2 + x[j]**2)))
                
        # Add a component that introduces fractal-like behavior with multiple scales
        fractal = 0
        for i in range(self.dim):
            fractal += (np.sin(10 * x[i]) * np.cos(5 * x[i]) + 0.5 * np.sin(20 * x[i])) * np.exp(-0.05 * x[i]**2)
            
        # Combine all components with modified weights to create a highly challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.15 * sinusoidal + 
                0.2 * chaotic_interaction + 
                0.3 * saddle + 
                0.25 * high_order + 
                0.15 * local_minima + 
                0.1 * cross_coupling + 
                0.05 * fractal + 
                7 * np.sum(np.sin(x)**4))  # Increased weight on sin^4 term
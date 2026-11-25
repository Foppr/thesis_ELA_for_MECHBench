import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced nested polynomial terms with higher degrees and more complex structure
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**8 + 4*x[i]**6 + 7*x[i]**4 + 3*x[i]**2) * np.sin(0.7 * x[i])
            
        # Sinusoidal component with enhanced chaotic phase modulation
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Enhanced chaotic interaction between dimensions using more complex coupling
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Enhanced saddle-point component with stronger non-convexity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**3 * np.exp(-0.3 * x[i]**2)
            
        # Enhanced high-order polynomial coupling with sinusoidal modulation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.3 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Enhanced local minima component with more varied depth and positioning
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(12 * x[i]) + 0.3 * np.sin(18 * x[i])
            
        # Add a component that introduces multiple local minima with varying depths and positions
        multi_minima = 0
        for i in range(self.dim):
            multi_minima += (np.sin(4 * x[i])**2 + 0.5 * np.cos(8 * x[i])) * np.exp(-0.2 * x[i]**2)
            
        # Combine all components with adjusted weights to create a more challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.2 * sinusoidal + 
                0.18 * chaotic_interaction + 
                0.28 * saddle + 
                0.32 * high_order + 
                0.12 * local_minima + 
                0.15 * multi_minima + 
                4 * np.sum(np.sin(x)**4))
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
            poly_nested += (x[i]**7 + 4*x[i]**5 + 6*x[i]**3 + 2*x[i]) * np.sin(0.6 * x[i])
            
        # Modified sinusoidal component with increased phase modulation complexity
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Improved chaotic interaction between dimensions using more complex coupling
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range for increased difficulty
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Enhanced saddle-point component with additional nonlinearities
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.6 * x[i]**2) + 0.3 * np.sin(3 * x[i])
            
        # More complex high-order polynomial coupling with multiple sinusoidal modulations
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.3 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Enhanced local minima component with multiple frequency components
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(12 * x[i]) + 0.3 * np.cos(5 * x[i])
            
        # Additional chaotic modulation component
        chaos_mod = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < i+3:  # Limited cross-dimensional chaos
                    chaos_mod += np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Combine all components with adjusted weights to create a more challenging landscape
        return (0.25 * quadratic + 
                0.45 * poly_nested + 
                0.18 * sinusoidal + 
                0.2 * chaotic_interaction + 
                0.3 * saddle + 
                0.35 * high_order + 
                0.15 * local_minima + 
                0.1 * chaos_mod + 
                6 * np.sum(np.sin(x)**4))
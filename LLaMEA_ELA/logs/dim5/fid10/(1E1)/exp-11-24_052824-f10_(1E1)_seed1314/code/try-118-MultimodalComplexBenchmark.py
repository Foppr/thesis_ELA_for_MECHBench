import numpy as np

class MultimodalComplexBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with mixed degrees
        poly_base = np.sum(x**4) + 0.5 * np.sum(x**6) + 0.1 * np.sum(x**8)
        
        # Trigonometric components creating oscillations
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.5 * np.sin(7 * x[i])
            
        # Exponential decay with sinusoidal modulation
        exp_modulated = 0
        for i in range(self.dim):
            exp_modulated += np.exp(-0.5 * x[i]**2) * np.sin(1.5 * x[i]) * np.cos(0.8 * x[i])
            
        # Coupling terms between dimensions with varying strengths
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Saddle-like behavior with multiple peaks and valleys
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 2*x[i] + 1) * np.exp(-0.3 * x[i]**2) + 0.5 * (x[i]**4 - 2*x[i]**2)
            
        # High-frequency oscillatory component
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(15 * x[i]) * np.cos(10 * x[i]) + 0.3 * np.sin(25 * x[i])
            
        # Mixed interaction terms with different weights
        mixed_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if (i + j) % 3 == 0:
                    mixed_interaction += x[i] * x[j] * np.sin(x[i] + x[j])
                elif (i + j) % 3 == 1:
                    mixed_interaction += (x[i]**2 + x[j]**2) * np.cos(0.5 * x[i] * x[j])
                else:
                    mixed_interaction += x[i] * np.exp(-x[j]**2) * np.sin(2 * x[i])
                    
        # Final combination with carefully tuned weights
        return (0.4 * poly_base + 
                0.3 * trig_component + 
                0.2 * exp_modulated + 
                0.15 * coupling + 
                0.25 * saddle + 
                0.35 * high_freq + 
                0.1 * mixed_interaction + 
                3 * np.sum(np.cos(x)**4))
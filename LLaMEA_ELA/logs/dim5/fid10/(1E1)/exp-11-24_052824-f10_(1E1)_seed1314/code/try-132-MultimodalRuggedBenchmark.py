import numpy as np

class MultimodalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component with exponential decay
        spherical = np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Exponential decay with sinusoidal modulation
        exp_modulated = 0
        for i in range(self.dim):
            exp_modulated += np.exp(-0.5 * x[i]**2) * np.sin(4 * x[i]) * np.cos(2 * x[i])
            
        # Multimodal component with multiple peaks
        multimodal = 0
        for i in range(self.dim):
            multimodal += (np.sin(5 * x[i]) + 0.5 * np.sin(10 * x[i])) * np.exp(-0.2 * x[i]**2)
            
        # High-frequency oscillation component
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(15 * x[i]) * np.cos(8 * x[i]) * (1 + 0.3 * np.sin(x[i]))
            
        # Radial symmetry breaking term
        radial_break = 0
        for i in range(self.dim):
            radial_break += (x[i]**4 - 2 * x[i]**2) * np.exp(-0.1 * x[i]**2)
            
        # Combine all components with carefully tuned weights
        return (0.3 * spherical + 
                0.25 * trig_coupling + 
                0.2 * exp_modulated + 
                0.15 * multimodal + 
                0.1 * high_freq + 
                0.05 * radial_break + 
                3 * np.sum(np.sin(x)**6))  # Added higher-order sine term for increased complexity
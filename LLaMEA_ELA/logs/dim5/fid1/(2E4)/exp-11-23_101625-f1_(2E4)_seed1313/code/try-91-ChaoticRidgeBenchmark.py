import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Chaotic ridge structures with dynamic heights and widths
        ridge_heights = 3.0 + 1.5 * np.sin(np.arange(self.dim) * 0.5)
        ridge_widths = 0.8 + 0.4 * np.cos(np.arange(self.dim) * 0.3)
        
        for i in range(self.dim):
            # Dynamic ridge with chaotic modulation
            ridge_mod = 1.0 + 0.3 * np.sin(i * 0.4 + np.sum(x**2) * 0.1)
            result += ridge_heights[i] * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(ridge_mod * i)) / (ridge_widths[i] * ridge_mod))**2)
            
        # Asymmetric coupling terms with time-varying interaction
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    # Asymmetric coupling with chaotic frequency modulation
                    freq_mod = 1.0 + 0.2 * np.sin(i * j * 0.3 + np.sum(x**2) * 0.05)
                    coupling += (x[i]**2 + x[j]**2) * np.sin(freq_mod * (x[i] - x[j])) * (1 + 0.1 * np.cos(i * 0.2))
            result += 0.2 * coupling
            
        # Time-varying harmonic interference
        time_factor = 1.0 + 0.5 * np.sin(np.sum(x**2) * 0.1)
        for i in range(self.dim):
            scale = 2**(i % 4 + 1) * time_factor
            result += 0.8 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.4) * (1 + 0.1 * np.sin(i * 0.3))
            
        # Dynamic barrier penalties with chaotic positioning
        barrier_positions = 4.0 * np.sin(np.arange(self.dim) * 0.5 + np.sum(x**2) * 0.08)
        barrier_heights = 2.0 + 1.0 * np.cos(np.arange(self.dim) * 0.4 + np.sum(x**2) * 0.1)
        
        for i in range(self.dim):
            distance_to_barrier = np.abs(np.abs(x[i]) - np.abs(barrier_positions[i]))
            if distance_to_barrier < 1.5:
                result += barrier_heights[i] * np.log(1 + 5 * distance_to_barrier**2)
                
        # Exponential penalty with asymmetric scaling
        penalty_scale = 1.5 + 0.8 * np.cos(np.sum(x**2) * 0.15)
        for i in range(self.dim):
            result += penalty_scale * np.exp(2.0 * abs(x[i]) / 5.0) * (1 + 0.15 * np.sin(x[i] * 3.0))
            
        # Additional chaotic harmonic interference
        chaos_factor = 0.2 * np.cos(np.sum(x**2) * 0.2 + 0.5 * np.sin(np.sum(x**2) * 0.15))
        for i in range(self.dim):
            result += 0.4 * np.sin(7.0 * x[i] + chaos_factor) * np.cos(4.0 * x[i] + chaos_factor)
            
        return result
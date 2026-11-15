import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dynamic scaling factors
        self.scaling_factors = np.array([np.exp(-0.1 * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Multi-modal component with sinusoidal modulations
        for i in range(self.dim):
            result += 0.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Exponentially decaying correlation structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.1 * np.abs(i - j))
                result += 0.3 * x[i] * x[j] * decay
                
        # Dynamic scaling with time-varying factors
        time_factor = np.sin(np.sum(x) * 0.2) + 1.5
        for i in range(self.dim):
            result += 0.4 * np.sin(x[i] * time_factor) * np.cos(x[i] * time_factor * 0.5)
            
        # Multi-scale oscillatory terms with varying frequencies
        freqs = np.array([2.0 + 3.0 * np.sin(i * 0.5) for i in range(self.dim)])
        for i in range(self.dim):
            result += 0.25 * np.sin(freqs[i] * x[i]) * np.cos(freqs[i] * x[i] * 0.3)
            
        # Chaotic interaction terms with fractal-like behavior
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(x[i] * np.exp(-0.03 * i))
        result += 0.35 * np.sin(chaotic_sum * 2.0) * np.cos(chaotic_sum * 0.7)
        
        # Asymmetric ruggedness with varying amplitudes
        for i in range(self.dim):
            amp = 0.5 + 0.3 * np.sin(i * 0.4)
            result += amp * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Memory-dependent component
        if hasattr(self, 'history'):
            mem_influence = 0.0
            for i in range(self.dim):
                mem_influence += 0.1 * self.history[i] * np.sin(x[i] * 0.3)
            result += mem_influence
        self.history = x.copy()
        
        # Global minimum attractor with dynamic scaling
        global_min = 0.0
        for i in range(self.dim):
            global_min += 0.1 * np.cos(0.5 * x[i]) * np.exp(-0.01 * x[i]**2)
        result += global_min
        
        # High-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.15 * np.sin(15.0 * x[i]) * np.cos(8.0 * x[i])
        result += noise
        
        # Add a complex non-separable interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.05 * x[i] * x[j] * x[k] * np.sin(x[i] + x[j] + x[k])
                    
        return result
import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Rugged component with modified exponentially decaying correlation structure
        for i in range(self.dim):
            result += 0.6 * np.exp(-0.15 * np.abs(x[i])) * np.sin(2.5 * np.pi * x[i])
            
        # Chaotic phase interactions with stronger non-linear coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.07 * i))
        result += 0.4 * np.sin(phase_sum) * np.cos(phase_sum * 0.6)
        
        # Multi-scale oscillatory terms with enhanced frequency variations
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(i * 0.4)
            amp = 1.2 + 0.3 * np.cos(i * 0.2)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Cross-dimensional interaction with modified exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.03 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper peaks
        for i in range(self.dim):
            result += 0.15 * np.sin(12 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.015 * x[i]**2)
            
        # Additional chaotic component with dynamic scaling
        dynamic_scale = np.sum(np.sin(x)**2) + 1.2
        result += 0.25 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.4 * dynamic_scale)
        
        # Non-separable high-order interactions with increased influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.08 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Improved global minimum enforcing with logarithmic penalty
        result += 0.02 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Add a new global minimum attractor term
        result += 0.1 * np.prod(np.cos(0.5 * x))
        
        # Introduce novel saddle point landscape with enhanced flat regions
        flat_region_penalty = 0.0
        for i in range(self.dim):
            flat_region_penalty += 0.3 * np.sin(0.5 * x[i])**4 + 0.2 * np.cos(0.3 * x[i])**3
        result += flat_region_penalty
        
        # Add high-order non-separable coupling with chaotic modulation
        coupling_modulation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        coupling_modulation += 0.05 * x[i] * x[j] * x[k] * x[l] * np.sin(x[i] + x[j] + x[k] + x[l])
        result += coupling_modulation
        
        # Introduce a novel penalty term that creates a complex basin of attraction
        basin_penalty = 0.0
        for i in range(self.dim):
            basin_penalty += 0.1 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.02 * np.abs(x[i]))
        result += basin_penalty
        
        # Add a dynamic chaotic noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += 0.08 * np.sin(x[i] * np.pi * np.exp(-0.1 * i)) * np.cos(x[i] * np.pi * np.exp(-0.1 * i))
        result += noise_component
        
        # Introduce a new penalty that emphasizes the difficulty of escaping local minima
        escape_penalty = 0.0
        for i in range(self.dim):
            escape_penalty += 0.2 * np.sin(8 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.01 * x[i]**2)
        result += escape_penalty
        
        return result
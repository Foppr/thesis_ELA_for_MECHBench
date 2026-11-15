import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.38) * np.cos(i * 0.72) for i in range(dim)])
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced rugged component with sharper peaks
        for i in range(self.dim):
            result += 0.82 * np.exp(-0.18 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Chaotic phase interactions with stronger coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.11 * i))
        result += 0.61 * np.sin(phase_sum) * np.cos(phase_sum * 0.68)
        
        # Multi-scale oscillatory terms with increased frequency variations
        for i in range(self.dim):
            freq = 2.1 + 3.8 * np.sin(i * 0.42)
            amp = 1.31 + 0.39 * np.cos(i * 0.28)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.42)
            
        # Cross-dimensional interaction with modified exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.038 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper peaks
        for i in range(self.dim):
            result += 0.21 * np.sin(14.1 * x[i]) * np.cos(7.2 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Additional chaotic component with dynamic scaling
        dynamic_scale = np.sum(np.sin(x)**2) + 1.18
        result += 0.32 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.41 * dynamic_scale)
        
        # Non-separable high-order interactions with increased influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.105 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Improved global minimum enforcing with logarithmic penalty
        result += 0.028 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Add a new global minimum attractor term
        result += 0.14 * np.prod(np.cos(0.58 * x))
        
        # Introduce enhanced noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.38 * np.sin(12.3 * x[i]) * np.cos(6.1 * x[i]) * np.exp(-0.062 * i)
        result += noise
        
        # Add dynamic basin complexity with time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.15) + 1.0
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.38))
        
        # Introduce multi-scale chaotic basin boundaries
        for i in range(self.dim):
            result += 0.26 * np.sin(9.2 * x[i]) * np.cos(4.6 * x[i]) * np.exp(-0.027 * np.abs(x[i]))
            
        # Add high-frequency oscillatory noise
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.14 * np.sin(23.1 * x[i]) * np.cos(11.5 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.7 * x[i]) * np.cos(1.8 * x[i])
        result += 0.16 * fractal_term
        
        # Memory-dependent fitness evaluation with historical influence
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.068 * self.history[i] * np.sin(x[i] * 0.62)
            result += hist_influence
        self.history = x.copy()
        
        # Add a complex multi-modal structure with memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.102 * np.sin(6.1 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.014 * np.abs(x[i]))
        result += multi_modal
        
        return result
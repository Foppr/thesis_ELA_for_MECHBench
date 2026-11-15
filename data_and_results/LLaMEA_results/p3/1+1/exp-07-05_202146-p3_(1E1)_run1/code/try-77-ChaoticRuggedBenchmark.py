import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like coefficients for self-similarity
        self.fractal_coeffs = np.array([np.sin(i * 0.3) * np.cos(i * 0.7) for i in range(dim)])
        
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
        
        # Introduce enhanced noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * i)
        result += noise
        
        # Add dynamic basin complexity with time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.1) + 1.0
        result += 0.15 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.3))
        
        # Introduce multi-scale chaotic basin boundaries
        for i in range(self.dim):
            result += 0.2 * np.sin(8 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.02 * np.abs(x[i]))
            
        # Add high-frequency oscillatory noise
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.1 * np.sin(20 * x[i]) * np.cos(10 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.0 * x[i]) * np.cos(1.5 * x[i])
        result += 0.12 * fractal_term
        
        # Memory-dependent fitness evaluation with historical influence
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.05 * self.history[i] * np.sin(x[i] * 0.5)
            result += hist_influence
        self.history = x.copy()
        
        # Add a complex multi-modal structure with memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.08 * np.sin(5 * x[i]) * np.cos(2.5 * x[i]) * np.exp(-0.01 * np.abs(x[i]))
        result += multi_modal
        
        return result
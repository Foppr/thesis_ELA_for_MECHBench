import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with modified sinusoidal components
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.35 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i])
            
        # Stronger phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.83 * np.sin(phase_sum) * np.cos(phase_sum * 0.91)
        
        # Multi-scale oscillatory terms with increased frequency and amplitude variations
        for i in range(self.dim):
            freq = 2.3 + 5.8 * np.sin(i * 0.47)
            amp = 1.57 + 0.68 * np.cos(i * 0.32)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.53)
            
        # Cross-dimensional interactions with exponential decay and higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.068 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper and more numerous peaks with asymmetric ruggedness
        for i in range(self.dim):
            result += 0.29 * np.sin(17.4 * x[i]) * np.cos(8.7 * x[i]) * np.exp(-0.024 * x[i]**2)
            
        # Dynamic scaling with enhanced chaotic attractor influence
        dynamic_scale = np.sum(np.sin(x)**2) + 1.53
        result += 0.41 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.58 * dynamic_scale)
        
        # Increased non-separability with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.147 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Enhanced global minimum enforcing with logarithmic and power penalty
        result += 0.038 * np.sum(np.log(1.0 + np.abs(x)) + np.abs(x)**0.7)
        
        # New global minimum attractor with complex trigonometric structure
        result += 0.18 * np.prod(np.cos(0.87 * x)) * np.exp(-0.015 * np.sum(x**2))
        
        # Introduce robust noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.51 * np.sin(15.3 * x[i]) * np.cos(7.6 * x[i]) * np.exp(-0.072 * i)
        result += noise
        
        # Dynamic basin complexity with time-varying attractors and multi-scale influence
        time_factor = np.sin(np.sum(x) * 0.19) + 1.0
        result += 0.26 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.42))
        
        # Multi-scale chaotic basin boundaries with enhanced complexity
        for i in range(self.dim):
            result += 0.31 * np.sin(11.2 * x[i]) * np.cos(5.6 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with enhanced amplitude
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(27.6 * x[i]) * np.cos(13.8 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with modified coefficients and scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.21 * fractal_term
        
        # Memory-dependent fitness with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.087 * self.history[i] * np.sin(x[i] * 0.71)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects and enhanced non-linearity
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.134 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.018 * np.abs(x[i]))
        result += multi_modal
        
        # Add a new hyper-chaotic component with multi-dimensional coupling
        hyper_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hyper_term += 0.05 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        result += hyper_term
        
        # Add a global minimum attractor with enhanced basin complexity
        result += 0.07 * np.sum(np.sin(2.5 * x) * np.cos(1.25 * x) * np.exp(-0.005 * x**2))
        
        return result
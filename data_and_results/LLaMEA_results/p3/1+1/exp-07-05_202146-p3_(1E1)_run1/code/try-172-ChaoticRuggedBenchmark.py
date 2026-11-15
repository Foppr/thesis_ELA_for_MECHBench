import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.73) * np.cos(i * 0.91) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with multi-scale oscillations
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.35 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i]) * np.cos(1.9 * np.pi * x[i])
            
        # Dynamic phase interactions with time-varying coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i)) * np.cos(x[i] * 0.31)
        result += 0.85 * np.sin(phase_sum * 0.67) * np.cos(phase_sum * 0.42)
        
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 2.3 + 5.7 * np.sin(i * 0.45)
            amp = 1.56 + 0.68 * np.cos(i * 0.32)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.52)
            
        # Cross-dimensional interaction with power-law decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = (1.0 + 0.1 * (i + j))**(-1.5)
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper peaks and valleys
        for i in range(self.dim):
            result += 0.27 * np.sin(17.4 * x[i]) * np.cos(8.7 * x[i]) * np.exp(-0.023 * x[i]**2)
            
        # Dynamic scaling chaotic component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.53
        result += 0.41 * np.sin(np.sum(x) * dynamic_scale * 0.83) * np.cos(np.sum(x) * 0.58 * dynamic_scale)
        
        # High-order non-separable interactions with variable influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.14 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.71)
                    
        # Global minimum enforcing with enhanced logarithmic penalty
        result += 0.042 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with fractal-like structure
        result += 0.19 * np.prod(np.cos(0.81 * x)) * np.exp(-0.015 * np.sum(x**2))
        
        # Enhanced noise and perturbation components with dynamic amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.52 * np.sin(15.3 * x[i]) * np.cos(7.6 * x[i]) * np.exp(-0.079 * i)
        result += noise
        
        # Dynamic basin complexity with multi-time scale attractors
        time_factor = np.sin(np.sum(x) * 0.17) + 1.2
        result += 0.28 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.41))
        
        # Multi-scale chaotic basin boundaries with varying amplitude
        for i in range(self.dim):
            result += 0.31 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with variable frequency
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.7 * x[i]) * np.cos(12.8 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity with enhanced complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i])
        result += 0.21 * fractal_term
        
        # Memory-dependent fitness with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.097 * self.history[i] * np.sin(x[i] * 0.72)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with enhanced memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.134 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.018 * np.abs(x[i]))
        result += multi_modal
        
        # Additional chaotic basin boundary with hyperbolic tangent modulation
        boundary_term = 0.0
        for i in range(self.dim):
            boundary_term += 0.23 * np.tanh(2.3 * x[i]) * np.cos(1.1 * x[i]) * np.exp(-0.029 * np.abs(x[i]))
        result += boundary_term
        
        # Cross-dimensional power interactions with dynamic weights
        power_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                power_interaction += 0.08 * (x[i]**1.7) * (x[j]**1.3) * np.sin(x[i] + x[j])
        result += power_interaction
        
        return result
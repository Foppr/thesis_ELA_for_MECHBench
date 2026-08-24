import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.57) * np.cos(i * 0.83) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with stronger non-linearity
        for i in range(self.dim):
            result += 0.85 * np.exp(-0.32 * np.abs(x[i])) * np.sin(3.7 * np.pi * x[i])
            
        # Dynamic phase interactions with time-varying coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.68 * np.sin(phase_sum * 1.2) * np.cos(phase_sum * 0.85)
        
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 2.3 + 5.7 * np.sin(i * 0.45)
            amp = 1.45 + 0.58 * np.cos(i * 0.31)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.52)
            
        # Cross-dimensional interaction with complex exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.065 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper and more numerous peaks
        for i in range(self.dim):
            result += 0.24 * np.sin(15.7 * x[i]) * np.cos(7.9 * x[i]) * np.exp(-0.023 * x[i]**2)
            
        # Dynamic scaling chaotic component
        dynamic_scale = np.sum(np.sin(x)**2) + 1.47
        result += 0.37 * np.sin(np.sum(x) * dynamic_scale * 0.8) * np.cos(np.sum(x) * 0.52 * dynamic_scale)
        
        # High-order non-separable interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        result += 0.12 * x[i] * x[j] * x[k] * x[l] * np.sin(x[i] * x[j] * x[k] * x[l])
                        
        # Global minimum enforcing with enhanced logarithmic penalty
        result += 0.035 * np.sum(np.log(1.0 + np.abs(x)))
        
        # New global minimum attractor with multi-dimensional cosine product
        result += 0.18 * np.prod(np.cos(0.78 * x))
        
        # Enhanced noise and perturbation with frequency doubling
        noise = 0.0
        for i in range(self.dim):
            noise += 0.42 * np.sin(14.3 * x[i]) * np.cos(7.15 * x[i]) * np.exp(-0.071 * i)
        result += noise
        
        # Dynamic basin complexity with dual attractors
        time_factor = np.sin(np.sum(x) * 0.17) + 1.0
        result += 0.24 * np.sum(np.sin(x * time_factor * 1.3) * np.cos(x * time_factor * 0.41))
        
        # Multi-scale chaotic basin boundaries with amplitude modulation
        for i in range(self.dim):
            result += 0.31 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i]))
            
        # High-frequency oscillatory noise with phase shifting
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.18 * np.sin(25.6 * x[i]) * np.cos(12.8 * x[i]) * np.sin(i * 0.23)
        result += freq_noise
        
        # Fractal-like self-similarity with higher-order terms
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.05 * x[i])
        result += 0.19 * fractal_term
        
        # Memory-dependent fitness with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.083 * self.history[i] * np.sin(x[i] * 0.71)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects and phase coupling
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.124 * np.sin(7.3 * x[i]) * np.cos(3.65 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Add a new chaotic basin boundary with irregularity
        irregularity = 0.0
        for i in range(self.dim):
            irregularity += 0.28 * np.sin(9.4 * x[i]) * np.cos(4.7 * x[i]) * np.exp(-0.028 * np.abs(x[i])) * np.sin(i * 0.37)
        result += irregularity
        
        # Add a high-dimensional interaction term with exponential weighting
        high_dim_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.08 * (i + j)**1.2)
                high_dim_interaction += weight * x[i] * x[j] * np.sin(x[i] * x[j] * 1.5)
        result += 0.15 * high_dim_interaction
        
        return result
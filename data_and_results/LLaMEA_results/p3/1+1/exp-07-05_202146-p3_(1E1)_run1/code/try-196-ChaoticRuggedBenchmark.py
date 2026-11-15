import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.57) * np.cos(i * 0.83) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced chaotic ruggedness with modified sine-cosine interactions
        for i in range(self.dim):
            result += 0.85 * np.exp(-0.28 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i]) * np.cos(1.9 * np.pi * x[i])
            
        # Stronger phase coupling with dynamic scaling factors
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i)) * np.cos(x[i] * 0.35)
        result += 0.63 * np.sin(phase_sum) * np.cos(phase_sum * 0.81) * np.exp(-0.03 * np.abs(phase_sum))
        
        # Multi-scale oscillatory terms with variable frequency modulation
        for i in range(self.dim):
            freq = 2.1 + 5.3 * np.sin(i * 0.42)
            amp = 1.42 + 0.58 * np.cos(i * 0.31)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.52)
            
        # Cross-dimensional interaction with adaptive exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.057 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += decay * interaction
                
        # Sharper peak formation with enhanced non-linearity
        for i in range(self.dim):
            result += 0.24 * np.sin(15.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Dynamic global minimum attractor with time-varying strength
        dynamic_scale = np.sum(np.sin(x)**2) + 1.35
        result += 0.37 * np.sin(np.sum(x) * dynamic_scale * 0.87) * np.cos(np.sum(x) * 0.52 * dynamic_scale)
        
        # High-order non-separable interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.12 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k]) * np.cos(x[i] + x[j] + x[k])
                    
        # Global minimum enforcing with enhanced logarithmic penalty
        result += 0.035 * np.sum(np.log(1.0 + np.abs(x)) * np.exp(-0.015 * np.abs(x)))
        
        # Additional global minimum attractor with multi-scale cosine product
        result += 0.15 * np.prod(np.cos(0.78 * x)) * np.exp(-0.02 * np.sum(x**2))
        
        # Enhanced noise and perturbation with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.42 * np.sin(13.6 * x[i]) * np.cos(6.8 * x[i]) * np.exp(-0.072 * i)
        result += noise
        
        # Dynamic basin complexity with time-varying attractors and memory influence
        time_factor = np.sin(np.sum(x) * 0.17) + 1.0
        result += 0.22 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.41) * np.exp(-0.02 * np.abs(x)))
        
        # Multi-scale chaotic basin boundaries with variable scaling
        for i in range(self.dim):
            result += 0.29 * np.sin(10.2 * x[i]) * np.cos(5.1 * x[i]) * np.exp(-0.031 * np.abs(x[i])) * np.sin(x[i] * 0.23)
            
        # High-frequency oscillatory noise with dynamic amplitude
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(25.3 * x[i]) * np.cos(12.6 * x[i]) * np.exp(-0.067 * np.abs(x[i]))
        result += freq_noise
        
        # Fractal-like self-similarity with enhanced scaling and phase modulation
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(4.1 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.018 * np.abs(x[i]))
        result += 0.18 * fractal_term
        
        # Memory-dependent fitness evaluation with enhanced historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.082 * self.history[i] * np.sin(x[i] * 0.65) * np.cos(x[i] * 0.32)
        result += hist_influence
        self.history = x.copy()
        
        # Complex multi-modal structure with memory effects and phase coupling
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.11 * np.sin(7.2 * x[i]) * np.cos(3.6 * x[i]) * np.exp(-0.015 * np.abs(x[i])) * np.sin(x[i] * 0.41)
        result += multi_modal
        
        return result
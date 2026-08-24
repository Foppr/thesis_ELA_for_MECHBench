import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_coeffs = np.array([np.sin(i * 0.51) * np.cos(i * 0.73) for i in range(dim)])
        self.history = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = np.sum(x**2)
        
        # Enhanced ruggedness with sharper peaks and valleys
        for i in range(self.dim):
            result += 0.81 * np.exp(-0.27 * np.abs(x[i])) * np.sin(3.1 * np.pi * x[i])
            
        # Stronger chaotic phase interactions
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.12 * i))
        result += 0.63 * np.sin(phase_sum) * np.cos(phase_sum * 0.81)
        
        # Multi-scale oscillatory terms with increased frequency variations
        for i in range(self.dim):
            freq = 2.1 + 4.7 * np.sin(i * 0.42)
            amp = 1.35 + 0.49 * np.cos(i * 0.29)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.51)
            
        # Cross-dimensional interaction with modified exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.052 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper peaks
        for i in range(self.dim):
            result += 0.21 * np.sin(14.7 * x[i]) * np.cos(7.3 * x[i]) * np.exp(-0.021 * x[i]**2)
            
        # Additional chaotic component with dynamic scaling
        dynamic_scale = np.sum(np.sin(x)**2) + 1.32
        result += 0.34 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.49 * dynamic_scale)
        
        # Non-separable high-order interactions with increased influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.11 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Improved global minimum enforcing with logarithmic penalty
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Add a new global minimum attractor term
        result += 0.15 * np.prod(np.cos(0.71 * x))
        
        # Introduce enhanced noise and perturbation components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.41 * np.sin(12.3 * x[i]) * np.cos(6.1 * x[i]) * np.exp(-0.067 * i)
        result += noise
        
        # Add dynamic basin complexity with time-varying attractors
        time_factor = np.sin(np.sum(x) * 0.16) + 1.0
        result += 0.21 * np.sum(np.sin(x * time_factor) * np.cos(x * time_factor * 0.41))
        
        # Introduce multi-scale chaotic basin boundaries
        for i in range(self.dim):
            result += 0.27 * np.sin(9.5 * x[i]) * np.cos(4.7 * x[i]) * np.exp(-0.029 * np.abs(x[i]))
            
        # Add high-frequency oscillatory noise
        freq_noise = 0.0
        for i in range(self.dim):
            freq_noise += 0.15 * np.sin(24.1 * x[i]) * np.cos(12.0 * x[i])
        result += freq_noise
        
        # Fractal-like self-similarity component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_coeffs[i] * np.sin(3.8 * x[i]) * np.cos(1.9 * x[i])
        result += 0.17 * fractal_term
        
        # Memory-dependent fitness evaluation with historical influence
        hist_influence = 0.0
        for i in range(self.dim):
            hist_influence += 0.073 * self.history[i] * np.sin(x[i] * 0.65)
        result += hist_influence
        self.history = x.copy()
        
        # Add a complex multi-modal structure with memory effects
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.11 * np.sin(6.5 * x[i]) * np.cos(3.2 * x[i]) * np.exp(-0.015 * np.abs(x[i]))
        result += multi_modal
        
        # Add a new complex interaction term with varying weights
        complex_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.08 * np.sin(i * 0.33) * np.cos(j * 0.27)
                complex_interaction += weight * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        result += complex_interaction
        
        # Add a highly non-linear chaotic component with dynamic frequency
        chaotic_component = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(x[i] * 0.1)
            chaotic_component += 0.25 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        result += chaotic_component
        
        # Add a multi-scale fractal interaction with enhanced complexity
        fractal_complex = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_complex += 0.05 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.03 * np.abs(x[i] - x[j]))
        result += fractal_complex
        
        return result
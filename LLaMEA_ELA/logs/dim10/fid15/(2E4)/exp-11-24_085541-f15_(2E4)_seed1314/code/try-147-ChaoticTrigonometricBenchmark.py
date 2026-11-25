import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base trigonometric term with chaotic modulation
        result = np.sum(np.sin(x)**2) * 0.1
        
        # Chaotic sinusoidal components with dynamic frequencies and amplitudes
        chaos_sum = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.6 * i + 1.3) * np.cos(0.4 * i + 0.7)
            amp = 1.5 + 0.7 * np.sin(0.5 * i + 0.9)
            chaos_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6) + \
                        0.5 * np.cos(freq * x[i]) * np.sin(freq * x[i] * 0.4)
        result += 2.5 * chaos_sum
        
        # Adaptive polynomial chaos expansion with varying degrees
        poly_sum = 0.0
        for i in range(self.dim):
            deg = 3 + int(4 * np.sin(0.7 * i) ** 2)
            coeff = 1.0 + 0.5 * np.cos(0.6 * i)
            poly_sum += coeff * x[i]**deg
        result += 2.0 * poly_sum
        
        # Dynamic conditioning with time-like parameter and chaotic scaling
        cond_sum = 0.0
        for i in range(self.dim):
            t_param = 0.7 + 0.3 * np.sin(0.4 * i + 1.5)
            cond_factor = 1.2 + 0.8 * np.sin(0.8 * i + 1.1) * t_param
            cond_sum += cond_factor * x[i]**4
        result += 1.8 * cond_sum
        
        # Cross-dimensional coupling with chaotic interaction strengths and phase shifts
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                strength = 0.7 + 0.4 * np.sin(0.3 * (i + j) + 1.1)
                phase_shift = 0.3 * np.cos(0.5 * i + 0.8)
                cross_sum += strength * np.sin(x[i] * x[j] + phase_shift) * np.cos(x[i] + x[j] + phase_shift)
        result += 2.2 * cross_sum
        
        # Fractal-like recursive structure with exponential decay and multiple iterations
        fractal_sum = 0.0
        for i in range(self.dim):
            val = x[i]
            for k in range(1, 6):
                decay = np.exp(-0.3 * k)
                fractal_sum += decay * (val**(2*k) + 0.4 * np.sin(k * val) + 0.2 * np.cos(k * val))
                val = np.cos(val) * np.sin(val)
        result += 1.0 * fractal_sum
        
        # Memory effect with weighted dimension interactions and chaotic weights
        if self.dim > 1:
            mem_sum = 0.0
            for i in range(1, self.dim):
                weight = 0.8 + 0.4 * np.cos(0.5 * i + 0.5) * np.sin(0.3 * i + 0.7)
                mem_sum += weight * x[i-1] * x[i] * (np.sin(x[i-1] + x[i]) + 0.3 * np.cos(x[i-1] - x[i]))
            result += 1.5 * mem_sum
            
        # Exponential modulation with chaotic parameters and multiple exponential terms
        exp_mod = 0.0
        for i in range(self.dim):
            amp1 = 1.2 + 0.6 * np.sin(0.4 * i + 0.8)
            amp2 = 0.8 + 0.4 * np.cos(0.5 * i + 0.6)
            freq1 = 0.9 + 0.3 * np.cos(0.3 * i + 0.9)
            freq2 = 0.7 + 0.2 * np.sin(0.4 * i + 0.5)
            exp_mod += amp1 * np.exp(-freq1 * np.abs(x[i])) * np.cos(1.5 * x[i]) + \
                      amp2 * np.exp(-freq2 * np.abs(x[i])) * np.sin(1.3 * x[i])
        result += 1.8 * exp_mod
        
        # Additional high-frequency chaotic oscillations
        high_freq_sum = 0.0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(0.8 * i + 1.2)
            amp = 2.0 + 1.0 * np.cos(0.6 * i + 0.9)
            high_freq_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        result += 0.8 * high_freq_sum
        
        return result
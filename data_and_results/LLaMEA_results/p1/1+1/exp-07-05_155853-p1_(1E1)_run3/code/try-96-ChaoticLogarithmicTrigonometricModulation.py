import numpy as np

class ChaoticLogarithmicTrigonometricModulation:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic barrier components
        log_barrier_sum = 0
        for i in range(self.dim):
            barrier_center = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.3 * np.sin(i * 1.2)
            barrier_width = 0.5 + 0.5 * np.abs(np.cos(i * 0.7))
            log_barrier_sum += np.log(1.0 + np.abs(x[i] - barrier_center) / barrier_width)
        
        # Trigonometric wave interactions with dynamic amplitudes and frequencies
        wave_sum = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.9)
            freq = 2.0 + 1.5 * np.cos(i * 0.6)
            wave_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.2 * np.sin(2.0 * freq * x[i])
        
        # Adaptive polynomial modulations with chaotic exponents
        poly_mod = 0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.0 * np.sin(i * 0.8)
            poly_mod += 0.1 * x[i]**(int(exp_factor)) + 0.05 * x[i]**(int(exp_factor * 1.5)) + 0.01 * x[i]**(int(exp_factor * 2.0))
        
        # Cross-dimensional trigonometric couplings with chaotic weights
        cross_trig = 0
        for i in range(self.dim - 1):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)
            cross_trig += weight * np.sin(x[i] + x[i+1]) * np.cos(x[i] * x[i+1])
        
        # Chaotic exponential modulation with dynamic scaling
        exp_mod = 0
        for i in range(self.dim):
            scale = 0.5 + 0.5 * np.sin(i * 0.4)
            exp_mod += scale * np.exp(-0.5 * (x[i]**2)) * np.sin(0.3 * x[i])
        
        # Global chaotic phase modulation
        global_phase = np.sin(0.1 * np.sum(x)) * np.cos(0.2 * np.sum(x**2)) * np.sin(0.05 * np.sum(x**3))
        
        # Combine all components with chaotic scaling factors
        return 1.5 * log_barrier_sum + 1.0 * wave_sum + 0.8 * poly_mod + 0.6 * cross_trig + 0.4 * exp_mod + 0.2 * global_phase
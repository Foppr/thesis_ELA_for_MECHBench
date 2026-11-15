import numpy as np

class ExponentialWaveValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with spatially varying rates
        exp_decay = np.sum(1.5 * np.exp(-0.5 * np.abs(x)) * np.cos(1.2 * x) * np.sin(0.8 * x))
        
        # Trigonometric wave interference with dynamic phase shifts
        wave_interference = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.4 * i + 0.2 * np.sum(x))
            wave_interference += np.sin(2.0 * x[i] + phase_shift) * np.cos(1.5 * x[i] + 0.5 * phase_shift)
        
        # Gradient-based adaptive modulation with directional sensitivity
        gradient_mod = 0.0
        for i in range(self.dim):
            if i == 0:
                grad = 0.0
            else:
                grad = (x[i] - x[i-1]) / (1.0 + 0.1 * np.abs(x[i-1]))
            gradient_mod += grad * np.sin(1.8 * x[i] + 0.3 * np.cos(x[i-1]))
        
        # Multi-scale oscillatory component with amplitude and frequency modulation
        multi_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(0.6 * i)
            freq_mod = 1.0 + 0.1 * np.cos(0.5 * x[i])
            amp_mod = 1.0 + 0.15 * np.sin(0.3 * x[i])
            multi_scale += amp_mod * np.sin(freq_mod * x[i] * scale_factor) * np.cos(0.7 * x[i])
        
        # Adaptive coupling term with memory effects
        coupling = 0.0
        for i in range(self.dim):
            if i == 0:
                mem = x[i]
            else:
                mem = 0.5 * x[i] + 0.5 * x[i-1]
            coupling += np.exp(-0.2 * mem**2) * np.sin(1.4 * mem + 0.3 * np.cos(mem))
        
        # Combine all components with dynamic weights based on input magnitude
        weight_exp = 1.0 + 0.1 * np.sin(0.2 * np.sum(x))
        weight_wave = 1.0 + 0.05 * np.cos(0.3 * np.sum(x))
        weight_grad = 1.0 + 0.1 * np.sin(0.1 * np.sum(x))
        weight_multi = 1.0 + 0.08 * np.cos(0.25 * np.sum(x))
        weight_coupling = 1.0 + 0.12 * np.sin(0.15 * np.sum(x))
        
        result = weight_exp * exp_decay + weight_wave * wave_interference + weight_grad * gradient_mod + weight_multi * multi_scale + weight_coupling * coupling
        
        return result
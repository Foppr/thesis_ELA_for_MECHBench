import numpy as np

class ExponentialTrigonometricParabolicValleys:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with oscillating amplitudes
        exp_decay_sum = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.6)
            exp_decay_sum += amp * np.exp(-0.5 * (x[i] - i * 0.5)**2) * np.cos(2.0 * x[i])
        
        # Trigonometric wave interference with varying frequencies and phases
        wave_interf_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.4)
            phase = 0.2 * np.cos(i * 0.7)
            wave_interf_sum += np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase)
        
        # Adaptive parabolic valleys with dynamic curvatures and positions
        parab_valley_sum = 0
        for i in range(self.dim):
            curvature = 0.5 + 0.5 * np.sin(i * 0.3)
            position = -3.0 + 6.0 * (i / max(1, self.dim - 1)) + 0.4 * np.cos(i * 0.5)
            parab_valley_sum += curvature * (x[i] - position)**2
        
        # Dynamic conditioning with chaotic scaling factors
        cond_sum = 0
        for i in range(self.dim):
            scale = 1.0 + 0.4 * np.sin(i * 0.8)
            cond_sum += scale * x[i]**4
        
        # Saddle point distribution with alternating signs
        saddle_sum = 0
        for i in range(self.dim - 1):
            sign = (-1)**i
            saddle_sum += sign * x[i] * x[i+1]
        
        # Cross-dimensional interaction with polynomial coupling
        cross_poly = 0
        for i in range(self.dim - 2):
            cross_poly += (x[i] * x[i+1] * x[i+2])**2
        
        # Global harmonic modulation with multiple frequencies
        global_mod = np.sin(0.3 * np.sum(x)) * np.cos(0.2 * np.sum(x**2)) * np.sin(0.1 * np.sum(x**3))
        
        # Add a new chaotic component for enhanced ruggedness
        chaotic_rugged = 0
        for i in range(self.dim):
            chaotic_rugged += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with refined weights
        return 1.2 * exp_decay_sum + 0.9 * wave_interf_sum + 0.7 * parab_valley_sum + 0.5 * cond_sum + 0.3 * saddle_sum + 0.2 * cross_poly + 0.1 * global_mod + 0.15 * chaotic_rugged
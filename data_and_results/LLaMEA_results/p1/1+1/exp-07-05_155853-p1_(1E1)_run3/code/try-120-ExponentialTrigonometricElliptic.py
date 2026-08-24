import numpy as np

class ExponentialTrigonometricElliptic:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with oscillating amplitudes
        exp_decay = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.6)
            exp_decay += amp * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i))**2)
        
        # Trigonometric wave interference with dynamic phases
        wave_interf = 0
        for i in range(self.dim):
            phase = 0.2 * np.cos(i * 0.4) + 0.1 * np.sin(i * 0.3)
            wave_interf += np.sin(x[i] + phase) * np.cos(2.0 * x[i] + phase)
        
        # Adaptive elliptic contours with dynamic eccentricity
        elliptic = 0
        for i in range(self.dim - 1):
            ecc = 0.5 + 0.5 * np.sin(i * 0.5)
            elliptic += (x[i]**2 + ecc * x[i+1]**2) / (1.0 + ecc**2)
        
        # Dynamic conditioning with varying exponents
        cond = 0
        for i in range(self.dim):
            exp = 1.0 + 0.3 * np.sin(i * 0.7)
            cond += (x[i]**exp) / (1.0 + 0.1 * i)
        
        # Saddle-point distribution with chaotic positioning
        saddle = 0
        for i in range(self.dim):
            pos = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.3 * np.sin(i * 1.2)
            saddle += (x[i] - pos)**2 * np.cos(0.5 * x[i])
        
        # Cross-dimensional coupling with exponentially weighted interactions
        cross = 0
        for i in range(self.dim - 1):
            weight = np.exp(-0.1 * i)
            cross += weight * x[i] * x[i+1] * np.sin(0.3 * (x[i] + x[i+1]))
        
        # Global modulation with multi-scale sinusoidal patterns
        global_mod = np.sin(0.1 * np.sum(x)) * np.cos(0.05 * np.sum(x**2)) * np.sin(0.02 * np.sum(x**3))
        
        # Add a new hyperbolic tangent component for additional ruggedness
        tanh_comp = 0
        for i in range(self.dim):
            tanh_comp += np.tanh(x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with refined weights
        return 1.2 * exp_decay + 0.8 * wave_interf + 0.6 * elliptic + 0.4 * cond + 0.3 * saddle + 0.2 * cross + 0.1 * global_mod + 0.05 * tanh_comp
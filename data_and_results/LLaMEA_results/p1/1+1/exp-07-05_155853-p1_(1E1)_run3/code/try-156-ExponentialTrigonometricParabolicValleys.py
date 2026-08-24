import numpy as np

class ExponentialTrigonometricParabolicValleys:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with dynamic rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.sin(i * 0.6)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i])
        
        # Trigonometric wave interference with varying frequencies and amplitudes
        wave_interference = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.4)
            amp = 0.8 + 0.2 * np.cos(i * 0.7)
            wave_interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive parabolic valleys with dynamic curvatures and positions
        parabolic_valleys = 0
        for i in range(self.dim):
            curvature = 0.5 + 0.5 * np.sin(i * 0.5)
            position = -3.0 + 6.0 * (i / max(1, self.dim - 1)) + 0.3 * np.cos(i * 0.8)
            parabolic_valleys += curvature * (x[i] - position)**2
        
        # Dynamic conditioning with chaotic scaling factors
        conditioning = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.9)
            conditioning += scale * x[i]**2
        
        # Cross-dimensional dependencies with chaotic coupling weights
        cross_deps = 0
        for i in range(self.dim - 1):
            weight = 0.3 + 0.7 * np.abs(np.sin(i * 0.6))
            cross_deps += weight * x[i] * x[i+1]
        
        # Add a new chaotic modulation component
        chaotic_mod = np.sin(0.4 * np.sum(x**3)) * np.cos(0.3 * np.sum(x**2)) * np.exp(-0.1 * np.sum(np.abs(x)))
        
        # Introduce a new polynomial interaction term for enhanced ruggedness
        poly_interaction = 0
        for i in range(self.dim - 2):
            poly_interaction += 0.02 * (x[i] * x[i+1] * x[i+2])**2
        
        # Combine all components with refined scaling factors
        return 1.2 * exp_decay + 0.9 * wave_interference + 0.7 * parabolic_valleys + 0.5 * conditioning + 0.3 * cross_deps + 0.2 * chaotic_mod + 0.1 * poly_interaction
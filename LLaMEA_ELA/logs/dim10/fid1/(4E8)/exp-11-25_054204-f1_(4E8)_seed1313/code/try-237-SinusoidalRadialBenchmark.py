import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights for polynomial decay
        self.radial_weights = np.power(np.arange(1, dim + 1), -1.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Radial polynomial decay with sinusoidal modulation
        radial_term = np.sum(self.radial_weights * np.sin(x) * np.cos(2.0 * x))
        f2 = 0.5 * radial_term
        
        # Cross-dimensional resonance with harmonic coupling
        resonance = 0.0
        for i in range(self.dim - 1):
            resonance += np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        f3 = 0.3 * resonance
        
        # Multi-scale sinusoidal gratings with varying frequencies
        grating = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i / (self.dim + 1))
            grating += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        f4 = 0.4 * grating
        
        # Radial harmonic oscillation with exponential weighting
        radial_harmonic = 0.0
        for i in range(self.dim):
            radial_harmonic += np.sin(x[i]) * np.cos(3.0 * x[i]) * np.exp(-x[i]**2 / 10.0)
        f5 = 0.25 * radial_harmonic
        
        # Spherical coupling with cubic interaction
        spherical_coupling = 0.0
        for i in range(self.dim - 2):
            spherical_coupling += x[i] * x[i+1] * x[i+2] * np.sin(x[i]**2 + x[i+1]**2)
        f6 = 0.35 * spherical_coupling
        
        # Multi-dimensional phase modulation with logarithmic scaling
        phase_mod = 0.0
        for i in range(self.dim):
            phase_mod += np.sin(np.log(1 + np.abs(x[i])) * x[i])
        f7 = 0.2 * phase_mod
        
        # Adaptive frequency coupling with exponential decay
        freq_coupling = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 1))
            freq_coupling += weight * np.cos(x[i] * x[i+1]) * np.sin(2.0 * x[i])
        f8 = 0.3 * freq_coupling
        
        # Higher-order polynomial with sinusoidal modulation
        poly_sine = 0.0
        for i in range(self.dim):
            poly_sine += (x[i]**5) * np.sin(1.5 * x[i])
        f9 = 0.2 * poly_sine
        
        # Complex cross-dimensional interaction with inverse scaling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += np.sin(x[i] / (1.0 + x[i+1]**2)) * np.cos(x[i+1] / (1.0 + x[i]**2))
        f10 = 0.25 * cross_interaction
        
        # Fractal-like coupling with self-similar structure
        fractal_coupling = 0.0
        for i in range(self.dim - 3):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2] * x[i+3]) * np.cos(x[i]**2 + x[i+1]**2)
        f11 = 0.15 * fractal_coupling
        
        # Combined scaling factor
        scale_factor = 1.0 + 0.3 * np.sin(np.sum(x**2) / 20.0)
        
        # Final function value
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)
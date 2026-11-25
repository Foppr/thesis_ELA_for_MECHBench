import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with Hurst parameter modulation
        f1 = 0.0
        for i in range(self.dim):
            # Fractal noise with dimension-dependent Hurst parameter
            hurst = 0.3 + 0.4 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            # Approximate fractal Brownian motion using sum of harmonics
            fbm = 0.0
            for k in range(1, 6):
                freq = k * (1.0 + 0.3 * np.sin(0.4 * i + 0.1 * k))
                phase = 0.5 * np.cos(0.3 * i + 0.2 * k)
                fbm += (1.0 / k**hurst) * np.sin(freq * x[i] + phase)
            f1 += fbm**2
            
        # Adaptive elliptic conditioning with chaotic modulation
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Elliptic conditioning with time-varying axes
            a = 1.0 + 0.5 * np.sin(0.3 * i + 0.4 * r)
            b = 1.0 + 0.3 * np.cos(0.2 * i + 0.3 * r)
            # Modified elliptic function
            f2 += (x[i]**2 / a**2) + (x[i]**2 / b**2) * np.exp(-0.1 * x[i]**2)
            
        # Gradient-based saddle-point interactions with phase-shifted coupling
        f3 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Phase-shifted coupling strength
                    coupling_phase = 0.2 * np.sin(0.4 * (i - j) + 0.3 * r)
                    coupling_strength = 1.0 + 0.4 * np.cos(coupling_phase)
                    # Saddle-point interaction with gradient influence
                    grad_influence = np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    saddle_interaction = coupling_strength * np.sin(x[i] + x[j]) * grad_influence
                    saddle_sum += saddle_interaction
            f3 += saddle_sum
            
        # Modified coupling strengths with radial dependence
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Radial-dependent coupling strength
                    radial_coupling = 1.0 + 0.3 * np.sin(0.5 * (i - j) + 0.2 * r)
                    interaction = radial_coupling * np.cos(x[i] - x[j])**2
                    coupling_sum += interaction
            f4 += coupling_sum
            
        # Phase shift modifications with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.6 * i + 0.2 * r + 0.1 * np.cos(r))
            f5 += np.sin(x[i] + phase_shift)**3
            
        # Saddle-point potential with multi-scale harmonic components
        f6 = 0.0
        for i in range(self.dim):
            # Multi-scale harmonic interactions
            harmonic_sum = 0.0
            for k in range(1, 4):
                freq = k * (1.0 + 0.2 * np.sin(0.3 * i + 0.1 * k))
                harmonic = np.cos(freq * x[i])
                harmonic_sum += harmonic / k
            f6 += harmonic_sum**2
            
        # Boundary-sensitive potential with exponential decay
        f7 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.2 * np.sin(0.5 * i + 0.3 * r)
                f7 += boundary_factor * np.exp(-0.3 * (np.abs(x[i]) - 4.0))
                
        # Elliptic harmonic interactions with adaptive coefficients
        f8 = 0.0
        for i in range(self.dim):
            elliptic_term = 0.0
            for j in range(i+1, self.dim):
                # Adaptive coefficient based on radial distance
                coeff = 1.0 + 0.4 * np.sin(0.3 * (i + j) + 0.2 * r)
                interaction = coeff * np.cos(x[i] + x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                elliptic_term += interaction
            f8 += elliptic_term
            
        # Chaotic rotational symmetry with fractal-like structure
        f9 = 0.0
        for i in range(self.dim):
            # Fractal-like rotational pattern
            rotation_pattern = np.sin(2.0 * x[i] + 0.5 * r)
            f9 += (np.cos(rotation_pattern)**2 + np.sin(rotation_pattern)**2) * np.exp(-0.1 * x[i]**2)
            
        # Multi-dimensional phase-shifted harmonic resonance
        f10 = 0.0
        for i in range(self.dim):
            # Phase-shifted resonance with chaotic modulation
            phase_mod = 0.4 * np.sin(0.5 * i + 0.3 * r) + 0.2 * np.cos(0.4 * r)
            f10 += np.sin(3.0 * x[i] + phase_mod)**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
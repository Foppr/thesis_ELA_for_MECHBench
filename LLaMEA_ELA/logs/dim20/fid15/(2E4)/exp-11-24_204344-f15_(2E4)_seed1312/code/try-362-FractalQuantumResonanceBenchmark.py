import numpy as np

class FractalQuantumResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Fractal Brownian motion component with Hurst parameter modulation
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = 0.3 + 0.4 * np.sin(i * 0.6 + self.dim * 0.5)
            # Use a simple fractal-like sum of harmonics with varying amplitudes
            for k in range(1, 6):
                freq = k * (1.0 + 0.2 * np.sin(i * 0.3 + k * 0.4))
                amp = 1.0 / (k ** (1.0 + hurst))
                fbm_term += amp * np.sin(freq * x[i] + k * 0.5)
        
        # Quantum tunneling effect with probabilistic potential wells
        tunnel_term = 0.0
        for i in range(self.dim):
            # Create a periodic potential landscape with tunnelling probabilities
            potential = 2.0 * np.sin(x[i] * 0.5) + 1.5 * np.cos(x[i] * 0.3)
            prob = 1.0 / (1.0 + np.exp(-potential))
            tunnel_term += prob * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
        
        # Adaptive resonance network with frequency-dependent feedback
        resonance_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 1.5 * np.sin(i * 0.4 + self.dim * 0.3)
            amp = 1.0 + 0.8 * np.cos(i * 0.6 + self.dim * 0.2)
            # Add resonance feedback with previous dimensions
            feedback = 0.0
            if i > 0:
                feedback = 0.5 * np.sin(x[i-1] * 0.7) * np.cos(x[i-1] * 0.4)
            resonance_term += amp * np.sin(freq * x[i] + feedback) ** 2
        
        # Discontinuous gradient landscape with chaotic boundary conditions
        discontinuous_term = 0.0
        for i in range(self.dim):
            # Create a piecewise function with chaotic breakpoints
            break_point = np.sin(i * 0.5 + self.dim * 0.4) * 2.0
            if x[i] < break_point:
                value = np.sin(x[i] * 3.0) + 0.5 * np.cos(x[i] * 1.5)
            else:
                value = np.cos(x[i] * 2.0) - 0.3 * np.sin(x[i] * 0.8)
            discontinuous_term += value ** 2
        
        # Multi-scale periodic modulation with self-similar patterns
        periodic_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 2.0 * np.sin(i * 0.8 + self.dim * 0.6)
            period = 2.0 * np.pi / (scale + 0.5)
            periodic_term += np.sin(x[i] * period) * np.cos(x[i] * period * 0.7)
        
        # Dynamic conditioning with chaotic dimension coupling
        condition_term = 0.0
        for i in range(self.dim):
            # Use chaotic modulation for conditioning strength
            cond_strength = 1.0 + 0.6 * np.sin(i * 0.3 + self.dim * 0.5 + np.sin(x[i]))
            condition_term += cond_strength * (x[i] ** 3) * np.cos(x[i] * 0.4)
        
        # Combine all terms with chaotic weights
        total = (0.22 * fbm_term + 
                0.18 * tunnel_term + 
                0.20 * resonance_term + 
                0.15 * discontinuous_term + 
                0.13 * periodic_term + 
                0.12 * condition_term)
        
        # Apply chaotic global scaling factor
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.8 + np.sum(x) * 0.3)
        
        return total * global_scale
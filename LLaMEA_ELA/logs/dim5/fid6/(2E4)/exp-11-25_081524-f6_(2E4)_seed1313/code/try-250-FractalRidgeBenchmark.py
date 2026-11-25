import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like structure with self-similar patterns
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal frequency modulation with enhanced chaos
            freq = 2.0 + 3.0 * np.sin(0.5 * self.t + i * 0.3 + 0.1 * np.sin(2.0 * self.t))
            amp = 1.0 + 0.8 * np.cos(0.4 * self.t + i * 0.2 + 0.1 * np.cos(1.5 * self.t))
            # Multi-scale fractal pattern with sine and cosine components
            result += amp * (xi**2) * np.sin(freq * xi) * np.cos(0.2 * xi**3)
            
        # Dynamic ridge structures with varying orientations and enhanced coupling
        ridge_strength = 1.5 + 0.5 * np.sin(0.6 * self.t + 0.2 * np.sin(1.2 * self.t))
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                # Ridge-like interaction with elliptic shaping and time-varying strength
                dist = (x[i] - x[j])**2
                ridge = ridge_strength * np.exp(-dist/1.2) * np.sin(1.5 * (x[i] + x[j]) + 0.4 * self.t + 0.1 * np.sin(0.8 * self.t))
                result += ridge * (x[i]**2 + x[j]**2)
                
        # Time-varying elliptic shaping with dynamic eccentricity and enhanced nonlinearity
        ellipse_factor = 0.5 + 0.3 * np.cos(0.7 * self.t + 0.1 * np.sin(1.3 * self.t))
        for i in range(self.dim):
            xi = x[i]
            # Elliptic terms with varying eccentricity and additional sine modulation
            result += ellipse_factor * (xi**4) * np.sin(0.8 * xi + 0.3 * self.t + 0.1 * np.cos(1.1 * self.t)) * np.cos(0.6 * xi**2)
            
        # Multi-scale periodic modulation with chaotic phase shifts and enhanced amplitude
        mod_freq = 4.0 + 2.0 * np.sin(0.9 * self.t + 0.1 * np.cos(1.7 * self.t))
        mod_amp = 0.8 + 0.4 * np.cos(0.8 * self.t + 0.1 * np.sin(1.9 * self.t))
        modulation = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.6 * self.t + i * 0.4 + 0.1 * np.cos(2.3 * self.t))
            modulation += mod_amp * np.sin(mod_freq * x[i] + phase_shift) * (x[i]**3)
            
        # Adaptive weighting with improved balance
        w1 = 0.7 + 0.1 * np.sin(0.5 * self.t + 0.1 * np.cos(1.4 * self.t))
        w2 = 0.2 + 0.1 * np.cos(0.6 * self.t + 0.1 * np.sin(1.8 * self.t))
        w3 = 0.1 + 0.05 * np.sin(0.7 * self.t + 0.1 * np.cos(2.1 * self.t))
        
        # Added nonlinear interaction term for enhanced multimodality with adaptive coefficients
        nonlin_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coef = 0.3 + 0.1 * np.sin(0.5 * self.t + i * 0.2 + j * 0.3)
                nonlin_term += coef * np.sin(2.0 * (x[i]**2 + x[j]**2) + 0.5 * self.t + 0.1 * np.cos(1.6 * self.t)) * (x[i] * x[j])
        
        result = w1 * result + w2 * modulation + w3 * nonlin_term
        return result
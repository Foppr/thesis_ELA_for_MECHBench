import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        radial = np.sum((x**2) * np.exp(-0.1 * x**2))
        
        # Sinusoidal oscillations with varying frequencies
        sin_osc = np.sum(np.sin(3 * x) * np.cos(7 * x) * np.exp(-0.05 * x**2))
        
        # Enhanced cross-term interactions creating complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.exp(-0.12 * (x[i]**2 + x[j]**2)) * np.cos(0.5 * x[i] * x[j])
        
        # Modified multimodal component with shifted Gaussian peaks
        multimodal = 0.0
        for i in range(1, 7):
            center = np.full(self.dim, i * 0.4)
            multimodal += np.exp(-0.3 * np.sum((x - center)**2)) * np.sin(3 * np.pi * np.sum(x - center))
        
        # Add higher-order polynomial terms for increased nonlinearity
        cubic = 0.03 * np.sum(x**3)
        quartic = 0.008 * np.sum(x**4)
        
        # Modified global scaling with distance from origin
        distance = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.15 * distance + 0.02 * distance**2
        
        # Add chaotic modulation term with improved frequency
        chaotic = 0.12 * np.sum(np.sin(12 * x) * np.cos(6 * x))
        
        # Introduce additional chaotic modulation with different frequency
        chaotic2 = 0.08 * np.sum(np.sin(18 * x) * np.cos(4 * x) * np.exp(-0.02 * x**2))
        
        # Add a new component with exponential decay and sinusoidal modulation
        exp_sin = 0.22 * np.sum(np.exp(-0.25 * x**2) * np.sin(6 * x))
        
        # Add chaotic attractor-inspired component with modified parameters
        attractor = 0.0
        for i in range(self.dim):
            attractor += np.sin(2.5 * x[i]) * np.cos(3.5 * x[i]) * np.exp(-0.12 * x[i]**2) * np.sin(0.6 * np.sum(x**2))
        
        # Add a new highly oscillatory component with increased frequency
        high_freq = 0.35 * np.sum(np.sin(25 * x) * np.cos(12 * x) * np.exp(-0.01 * x**2))
        
        # Add a new chaotic spiral component for increased complexity
        spiral = 0.18 * np.sum(np.sin(10 * x) * np.cos(15 * x) * np.exp(-0.09 * x**2) * np.sin(0.35 * np.sum(x**2)))
        
        # Add a new interaction term with inverse distance scaling
        inv_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if abs(x[i] - x[j]) > 1e-10:
                    inv_interaction += np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) / (1.0 + abs(x[i] - x[j]))
        
        # Add a new component with fractional powers for increased complexity
        fractional = 0.28 * np.sum(np.abs(x)**1.6 * np.sin(4.5 * x))
        
        # Add a new component with periodic modulation based on sum of coordinates
        periodic_mod = 0.12 * np.sum(np.sin(2.5 * np.sum(x)) * np.cos(3.5 * np.sum(x)) * np.exp(-0.06 * x**2))
        
        # Add a new component with trigonometric interactions and exponential decay
        trig_exp = 0.2 * np.sum(np.sin(x) * np.cos(2.5 * x) * np.exp(-0.035 * x**2))
        
        # Add a new component with polynomial and sinusoidal interaction
        poly_sin = 0.25 * np.sum((x**2.5) * np.sin(3.5 * x) * np.exp(-0.045 * x**2))
        
        # Add a new component with double chaotic modulation
        double_chaotic = 0.15 * np.sum(np.sin(30 * x) * np.cos(8 * x) * np.sin(15 * x) * np.exp(-0.015 * x**2))
        
        # Add a new component with complex cross-dimensional interaction
        complex_cross = 0.1 * np.sum(np.sin(x) * np.cos(x**1.5) * np.exp(-0.07 * x**2))
        
        # Add a new component with logarithmic and exponential interaction
        log_exp = 0.18 * np.sum(np.log(1 + np.abs(x)) * np.exp(-0.025 * x**2))
        
        # Add a new component with hyperbolic and exponential interaction
        hyperbolic = 0.12 * np.sum(np.tanh(x) * np.exp(-0.06 * x**2))
        
        # Add a new component with modified Gaussian peaks and additional sinusoidal modulation
        enhanced_peaks = 0.0
        for i in range(1, 9):
            center = np.full(self.dim, i * 0.35)
            enhanced_peaks += np.exp(-0.25 * np.sum((x - center)**2)) * np.sin(4 * np.pi * np.sum(x - center)) * np.cos(2 * np.sum(x))
        
        # Add a new component with mixed trigonometric and polynomial terms
        mixed_terms = 0.15 * np.sum(np.sin(x**2) * np.cos(x) * np.exp(-0.04 * x**2))
        
        # Add a new component with modified Gaussian peaks and additional sinusoidal modulation
        new_peaks = 0.0
        for i in range(1, 10):
            center = np.full(self.dim, i * 0.3)
            new_peaks += np.exp(-0.2 * np.sum((x - center)**2)) * np.sin(5 * np.pi * np.sum(x - center)) * np.cos(3 * np.sum(x))
        
        # Add a new component with modified chaotic spiral
        new_spiral = 0.2 * np.sum(np.sin(12 * x) * np.cos(18 * x) * np.exp(-0.08 * x**2) * np.sin(0.4 * np.sum(x**2)))
        
        # Add a new component with modified inverse interaction
        new_inv_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if abs(x[i] - x[j]) > 1e-10:
                    new_inv_interaction += np.cos(x[i] + x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2)) / (1.0 + abs(x[i] - x[j])**2)
        
        # Combine all components with adjusted weights
        return radial + 0.85 * sin_osc + 0.5 * cross_term + 0.65 * multimodal + cubic + quartic + scaling + chaotic + chaotic2 + exp_sin + attractor + high_freq + spiral + 0.25 * inv_interaction + fractional + periodic_mod + trig_exp + poly_sin + double_chaotic + complex_cross + log_exp + hyperbolic + 0.3 * enhanced_peaks + 0.18 * mixed_terms + 0.22 * new_peaks + 0.25 * new_spiral + 0.15 * new_inv_interaction
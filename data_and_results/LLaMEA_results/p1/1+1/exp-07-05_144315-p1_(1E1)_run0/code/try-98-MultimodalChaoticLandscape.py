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
        sin_osc = np.sum(np.sin(3.5 * x) * np.cos(6.5 * x) * np.exp(-0.05 * x**2))
        
        # Enhanced cross-term interactions creating complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.exp(-0.12 * (x[i]**2 + x[j]**2)) * np.cos(0.4 * x[i] * x[j])
        
        # Modified multimodal component with shifted Gaussian peaks
        multimodal = 0.0
        for i in range(1, 7):
            center = np.full(self.dim, i * 0.35)
            multimodal += np.exp(-0.3 * np.sum((x - center)**2)) * np.sin(3.2 * np.pi * np.sum(x - center))
        
        # Add higher-order polynomial terms for increased nonlinearity
        cubic = 0.035 * np.sum(x**3)
        quartic = 0.009 * np.sum(x**4)
        
        # Modified global scaling with distance from origin
        distance = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.14 * distance + 0.022 * distance**2
        
        # Add chaotic modulation term with improved frequency
        chaotic = 0.11 * np.sum(np.sin(11.5 * x) * np.cos(5.8 * x))
        
        # Introduce additional chaotic modulation with different frequency
        chaotic2 = 0.07 * np.sum(np.sin(17.5 * x) * np.cos(3.9 * x) * np.exp(-0.02 * x**2))
        
        # Add a new component with exponential decay and sinusoidal modulation
        exp_sin = 0.23 * np.sum(np.exp(-0.24 * x**2) * np.sin(5.8 * x))
        
        # Add chaotic attractor-inspired component with modified parameters
        attractor = 0.0
        for i in range(self.dim):
            attractor += np.sin(2.4 * x[i]) * np.cos(3.4 * x[i]) * np.exp(-0.11 * x[i]**2) * np.sin(0.55 * np.sum(x**2))
        
        # Add a new highly oscillatory component with increased frequency
        high_freq = 0.34 * np.sum(np.sin(24.5 * x) * np.cos(11.8 * x) * np.exp(-0.01 * x**2))
        
        # Add a new chaotic spiral component for increased complexity
        spiral = 0.17 * np.sum(np.sin(9.8 * x) * np.cos(14.5 * x) * np.exp(-0.085 * x**2) * np.sin(0.33 * np.sum(x**2)))
        
        # Add a new interaction term with inverse distance scaling
        inv_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if abs(x[i] - x[j]) > 1e-10:
                    inv_interaction += np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) / (1.0 + abs(x[i] - x[j]))
        
        # Add a new component with fractional powers for increased complexity
        fractional = 0.27 * np.sum(np.abs(x)**1.55 * np.sin(4.3 * x))
        
        # Add a new component with periodic modulation based on sum of coordinates
        periodic_mod = 0.11 * np.sum(np.sin(2.4 * np.sum(x)) * np.cos(3.4 * np.sum(x)) * np.exp(-0.055 * x**2))
        
        # Add a new component with trigonometric interactions and exponential decay
        trig_exp = 0.21 * np.sum(np.sin(x) * np.cos(2.4 * x) * np.exp(-0.033 * x**2))
        
        # Add a new component with polynomial and sinusoidal interaction
        poly_sin = 0.26 * np.sum((x**2.4) * np.sin(3.4 * x) * np.exp(-0.043 * x**2))
        
        # Add a new component with double chaotic modulation
        double_chaotic = 0.14 * np.sum(np.sin(29.5 * x) * np.cos(7.8 * x) * np.sin(14.5 * x) * np.exp(-0.014 * x**2))
        
        # Add a new component with complex cross-dimensional interaction
        complex_cross = 0.11 * np.sum(np.sin(x) * np.cos(x**1.45) * np.exp(-0.065 * x**2))
        
        # Add a new component with logarithmic and exponential interaction
        log_exp = 0.17 * np.sum(np.log(1 + np.abs(x)) * np.exp(-0.023 * x**2))
        
        # Add a new component with hyperbolic and exponential interaction
        hyperbolic = 0.11 * np.sum(np.tanh(x) * np.exp(-0.055 * x**2))
        
        # Add a new component with modified Gaussian peaks and additional sinusoidal modulation
        enhanced_peaks = 0.0
        for i in range(1, 9):
            center = np.full(self.dim, i * 0.32)
            enhanced_peaks += np.exp(-0.24 * np.sum((x - center)**2)) * np.sin(3.9 * np.pi * np.sum(x - center)) * np.cos(1.9 * np.sum(x))
        
        # Add a new component with mixed trigonometric and polynomial terms
        mixed_terms = 0.14 * np.sum(np.sin(x**1.9) * np.cos(x) * np.exp(-0.038 * x**2))
        
        # Combine all components with adjusted weights
        return radial + 0.83 * sin_osc + 0.48 * cross_term + 0.63 * multimodal + cubic + quartic + scaling + chaotic + chaotic2 + exp_sin + attractor + high_freq + spiral + 0.24 * inv_interaction + fractional + periodic_mod + trig_exp + poly_sin + double_chaotic + complex_cross + log_exp + hyperbolic + 0.29 * enhanced_peaks + 0.17 * mixed_terms
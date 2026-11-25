import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced elliptic factors with higher variance and more irregular spacing
        self.elliptic_factors = np.logspace(1.0, 3.0, min(20, dim)) * 1.5
        # Modified saddle strengths for sharper transitions and more complex dynamics
        self.saddle_strengths = np.linspace(1.5, 5.0, min(15, dim)) * 1.5
        # Adjusted chaotic parameters for more complex modulation and better conditioning
        self.chaotic_params = np.random.uniform(0.3, 1.3, min(12, dim)) * 1.6
        # Fractal sine-wave interaction parameters with higher frequencies
        self.fractal_sine_params = np.logspace(1.2, 3.5, min(10, dim)) * 1.2
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced elliptic valley components with steeper curvature and more irregular shapes
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_factors), self.dim)):
            factor = self.elliptic_factors[i]
            # Steeper asymmetric elliptic shape with higher-order polynomial terms
            ellipse_val = factor * (x_norm[i] ** 2) + 0.7 * (x_norm[i] ** 4) + 0.2 * (x_norm[i] ** 6) + 0.08 * (x_norm[i] ** 8) + 0.03 * (x_norm[i] ** 10)
            elliptic_term += ellipse_val
            
        # Refined saddle-point corridors with stronger nonlinearity and more complex structure
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            # Enhanced saddle with cubic modulation and additional sinusoidal perturbations
            saddle_val = strength * x_norm[i] * np.sin(9.0 * x_norm[i]) + 0.3 * (x_norm[i] ** 3) + 0.15 * x_norm[i] * np.cos(7.0 * x_norm[i]) + 0.08 * np.sin(11.0 * x_norm[i])
            saddle_term += saddle_val
            
        # Modified chaotic interaction terms with increased coupling strength and frequency modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Stronger dynamic coupling with frequency modulation and phase shifts
                modulator = np.sin(self.chaotic_params[i % len(self.chaotic_params)] * 
                                 x_norm[j] * (i + 1) * 2.5 + np.pi / 3.0)
                coupling = 0.5 * (x_norm[i] ** 2) * (x_norm[j] ** 2) * modulator
                chaotic_term += coupling
                
        # Refined multi-scale optima clustering with increased separation and more complex structures
        cluster_term = 0.0
        for i in range(self.dim):
            # Increased clustering distance and sharper minima with sinusoidal positioning
            cluster_pos = 3.5 * np.sin(0.8 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            cluster_val = 1.5 * (distance ** 4) + 0.8 * (distance ** 6) + 0.25 * (distance ** 8) + 0.1 * (distance ** 10) + 0.05 * (distance ** 12)
            cluster_term += cluster_val
            
        # Fractal sine-wave interactions for enhanced multimodality and complexity
        fractal_sine_term = 0.0
        for i in range(self.dim):
            freq = self.fractal_sine_params[i % len(self.fractal_sine_params)]
            fractal_val = 0.4 * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] ** 2) + 0.2 * np.sin(2 * freq * x_norm[i]) + 0.1 * np.cos(3 * freq * x_norm[i])
            fractal_sine_term += fractal_val
            
        # Combined terms with adjusted weights for increased difficulty and better conditioning
        result = 1.1 * elliptic_term + 0.9 * saddle_term + 0.8 * chaotic_term + 0.7 * cluster_term + 0.6 * fractal_sine_term
        
        # Add enhanced dynamic noise with adaptive amplitude based on dimensionality
        noise_amplitude = 0.06 * (1.0 + 0.12 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise
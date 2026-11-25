import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced elliptic factors with higher variance and more irregular spacing
        self.elliptic_factors = np.logspace(0.8, 2.5, min(15, dim)) * 1.3
        # Modified saddle strengths for sharper transitions and more complex dynamics
        self.saddle_strengths = np.linspace(1.2, 4.5, min(12, dim)) * 1.2
        # Adjusted chaotic parameters for more complex modulation and better conditioning
        self.chaotic_params = np.random.uniform(0.2, 1.1, min(10, dim)) * 1.4
        # Fractal sine-wave interaction parameters
        self.fractal_sine_params = np.logspace(1.0, 3.0, min(8, dim)) * 0.8
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced elliptic valley components with steeper curvature and more irregular shapes
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_factors), self.dim)):
            factor = self.elliptic_factors[i]
            # Steeper asymmetric elliptic shape with higher-order polynomial terms
            ellipse_val = factor * (x_norm[i] ** 2) + 0.6 * (x_norm[i] ** 4) + 0.15 * (x_norm[i] ** 6) + 0.05 * (x_norm[i] ** 8)
            elliptic_term += ellipse_val
            
        # Refined saddle-point corridors with stronger nonlinearity and more complex structure
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            # Enhanced saddle with cubic modulation and additional sinusoidal perturbations
            saddle_val = strength * x_norm[i] * np.sin(7.0 * x_norm[i]) + 0.25 * (x_norm[i] ** 3) + 0.1 * x_norm[i] * np.cos(5.0 * x_norm[i])
            saddle_term += saddle_val
            
        # Modified chaotic interaction terms with increased coupling strength and frequency modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Stronger dynamic coupling with frequency modulation and phase shifts
                modulator = np.sin(self.chaotic_params[i % len(self.chaotic_params)] * 
                                 x_norm[j] * (i + 1) * 2.0 + np.pi / 4.0)
                coupling = 0.4 * (x_norm[i] ** 2) * (x_norm[j] ** 2) * modulator
                chaotic_term += coupling
                
        # Refined multi-scale optima clustering with increased separation and more complex structures
        cluster_term = 0.0
        for i in range(self.dim):
            # Increased clustering distance and sharper minima with sinusoidal positioning
            cluster_pos = 3.0 * np.sin(0.7 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            cluster_val = 1.2 * (distance ** 4) + 0.6 * (distance ** 6) + 0.15 * (distance ** 8) + 0.05 * (distance ** 10)
            cluster_term += cluster_val
            
        # Fractal sine-wave interactions for enhanced multimodality and complexity
        fractal_sine_term = 0.0
        for i in range(self.dim):
            freq = self.fractal_sine_params[i % len(self.fractal_sine_params)]
            fractal_val = 0.3 * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] ** 2) + 0.15 * np.sin(2 * freq * x_norm[i])
            fractal_sine_term += fractal_val
            
        # Combined terms with adjusted weights for increased difficulty and better conditioning
        result = 0.9 * elliptic_term + 0.7 * saddle_term + 0.6 * chaotic_term + 0.5 * cluster_term + 0.4 * fractal_sine_term
        
        # Add enhanced dynamic noise with adaptive amplitude based on dimensionality
        noise_amplitude = 0.04 * (1.0 + 0.08 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise
import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 3.9  # Logistic map parameter
        self.alpha = 0.5
        self.beta = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_value = np.sum(x**2)
        
        # Logistic map component for chaotic behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            # Simple logistic map iteration
            x_log = 0.5
            for _ in range(10):
                x_log = self.r * x_log * (1 - x_log)
            chaotic_term += x_log * np.sin(x[i])
        
        f_value += 0.3 * chaotic_term
        
        # Fractional polynomial terms with varying exponents
        for i in range(self.dim):
            # Use fractional exponents to create irregularity
            f_value += 0.2 * np.abs(x[i])**1.7 * np.cos(3 * x[i])
            
        # Spherical harmonics component in higher dimensions
        if self.dim >= 2:
            # Create a 2D spherical harmonic-like term
            r = np.sqrt(x[0]**2 + x[1]**2)
            theta = np.arctan2(x[1], x[0])
            f_value += 0.25 * np.sin(5 * r) * np.cos(3 * theta)
            
        if self.dim >= 3:
            # Add 3D spherical component
            r = np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
            phi = np.arctan2(np.sqrt(x[0]**2 + x[1]**2), x[2])
            theta = np.arctan2(x[1], x[0])
            f_value += 0.2 * np.sin(4 * r) * np.cos(2 * phi) * np.sin(3 * theta)
            
        # Multi-scale sinusoidal modulation with chaotic frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(x[i] * 0.5)  # Chaotic frequency modulation
            f_value += 0.15 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Cross-variable interaction with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                # Chaotic modulation based on both variables
                mod_i = 1.0 + 0.3 * np.sin(x[i] * 0.3)
                mod_j = 1.0 + 0.3 * np.cos(x[j] * 0.4)
                f_value += 0.1 * np.sin(mod_i * x[i] + mod_j * x[j]) * np.cos(mod_i * x[i] - mod_j * x[j])
                
        # Fractional polynomial interaction terms
        for i in range(self.dim):
            f_value += 0.1 * np.abs(x[i])**1.3 * np.sin(2 * x[i])
            
        # Add a complex multi-modal component
        f_value += 0.2 * np.sum(np.sin(10 * x) + np.cos(15 * x) + np.sin(20 * x) + np.cos(25 * x))
        
        # Add a term that makes the function non-smooth in nature
        f_value += 0.15 * np.sum(np.abs(x)**1.9)
        
        return f_value
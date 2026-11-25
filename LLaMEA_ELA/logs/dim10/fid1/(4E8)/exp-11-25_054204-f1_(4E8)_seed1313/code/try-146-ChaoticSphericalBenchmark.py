import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients with increased complexity
        self.sphere_coeffs = np.random.uniform(-1, 1, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component with modified r parameter and feedback
        logistic_map = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                logistic_map += x[i] * (1 - x[i])
            else:
                logistic_map += x[i-1] * (1 - x[i-1]) * r
            # Add feedback term to increase complexity
            logistic_map += 0.1 * np.sin(x[i]) * np.cos(x[i-1]) if i > 0 else 0
        
        # Spherical harmonic interaction term with increased complexity and modified weights
        sph_harm = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                sph_harm += self.sphere_coeffs[i, j] * np.sin((i+1) * x[j]) * np.cos((j+1) * x[i]) * (i+1+j+1)
        
        # Adaptive sigmoidal scaling component with modified weights and additional terms
        sig_scale = 0.0
        for i in range(self.dim):
            sig_scale += 1.0 / (1.0 + np.exp(-x[i] * (i+2))) + 0.5 * np.sin(x[i] / (i+1))
        
        # Fractal-like polynomial with mixed degrees, added cosine modulation and interaction terms
        fractal_poly = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                fractal_poly += x[i]**(i+2) * np.cos(x[i]) + 0.1 * x[i] * np.sin(x[i])
            elif i % 3 == 1:
                fractal_poly += x[i]**(i+3) * np.sin(x[i]) + 0.2 * x[i]**2 * np.cos(x[i])
            else:
                fractal_poly += x[i]**(i+4) * np.tan(x[i] / 2.0) + 0.15 * x[i] * np.exp(-x[i]**2)
        
        # Enhanced cross-dimensional coupling with multiple interaction types and additional terms
        cross_coupling = 0.0
        for i in range(self.dim-1):
            cross_coupling += np.exp(-0.1 * (x[i] - x[i+1])**2) * np.cos(3.0 * x[i])
            cross_coupling += np.sin(0.5 * (x[i] + x[i+1])) * np.cos(2.0 * x[i])
            # Add additional coupling terms
            cross_coupling += 0.5 * np.sin(x[i] * x[i+1]) * np.cos(x[i]**2 + x[i+1]**2)
        
        # Additional harmonic coupling term with modified frequency and added dimensionality
        harmonic_coupling = 0.0
        for i in range(self.dim):
            harmonic_coupling += np.sin(x[i]) * np.cos(3.0 * x[i]) * (i+1) + 0.2 * np.cos(x[i]**2) * np.sin(x[i])
        
        # Novel coupling mechanism: interaction between all dimensions through a radial basis function with additional terms
        radial_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                radial_coupling += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                # Add additional interaction terms
                radial_coupling += 0.3 * np.cos(x[i] * x[j]) * np.sin(x[i]**2 - x[j]**2)
        
        # Modified polynomial terms with higher-order interactions, trigonometric modulation and noise terms
        poly_mod = 0.0
        for i in range(self.dim):
            poly_mod += (x[i]**(i+5)) * np.sin(x[i]/(i+1)) + (x[i]**(i+3)) * np.cos(x[i]/(i+2))
            # Add noise terms
            poly_mod += 0.1 * np.sin(x[i] * i) * np.cos(x[i] / (i+1))
        
        # Gaussian noise modulation with adaptive variance and additional interaction
        noise_mod = np.random.normal(0, 0.05) * np.sum(np.exp(-0.5 * x**2)) + 0.02 * np.sum(np.sin(x))
        
        # Add a new term that increases complexity and improves discrimination
        new_term = 0.0
        for i in range(self.dim):
            new_term += (x[i] - 1)**4 + (x[i] + 1)**4
        
        # Add an additional complexity term that enhances conditioning and algorithmic discrimination
        complexity_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                complexity_term += np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2) + 0.05 * np.tan(x[i] * x[j])
        
        # Add a novel chaotic modulation component with higher frequency oscillations
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.3 * np.tan(2 * x[i])
        
        # Add a high-order polynomial interaction term with fractal-like structure
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_interaction += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Combine all terms with adjusted weights to improve fitness score
        return 0.8 * logistic_map + 1.2 * sph_harm + 0.6 * sig_scale + 1.5 * fractal_poly + \
               1.3 * cross_coupling + 0.9 * harmonic_coupling + 1.1 * radial_coupling + \
               1.4 * poly_mod + 0.7 * noise_mod + 1.0 * new_term + 0.8 * complexity_term + \
               1.2 * chaotic_mod + 0.9 * fractal_interaction
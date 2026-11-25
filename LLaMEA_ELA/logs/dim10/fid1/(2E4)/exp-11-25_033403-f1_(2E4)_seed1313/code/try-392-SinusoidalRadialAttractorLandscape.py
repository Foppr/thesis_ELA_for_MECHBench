import numpy as np

class SinusoidalRadialAttractorLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize sinusoidal components with varying frequencies and amplitudes
        self.sin_freqs = np.random.uniform(1.0, 8.0, dim)
        self.sin_amps = np.random.uniform(0.5, 3.0, dim)
        # Initialize radial basis functions with random centers and variances
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (6, dim))
        self.rbf_vars = np.random.uniform(0.2, 2.0, (6, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.5, 6)
        # Initialize adaptive conditioning parameters
        self.conditioning_params = np.random.uniform(0.1, 2.0, dim)
        # Initialize dynamic attractor positions and strengths
        self.attractor_centers = np.random.uniform(-4.0, 4.0, (4, dim))
        self.attractor_strengths = np.random.uniform(1.0, 5.0, 4)
        # Initialize cross-dimensional coupling matrix with modified weights
        self.coupling_matrix = np.random.uniform(-0.25, 0.25, (dim, dim))
        # Initialize harmonic interaction terms
        self.harmonic_coeffs = np.random.uniform(0.2, 1.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute sinusoidal oscillations with varying frequencies and amplitudes
        sin_terms = 0.0
        for j in range(self.dim):
            sin_terms += self.sin_amps[j] * np.sin(self.sin_freqs[j] * x[j]) * np.cos(0.3 * x[j])
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(6):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute adaptive conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_params[j] * (x[j]**2) * (1.0 + 0.2 * np.sin(3.0 * x[j]))
        
        # Compute dynamic attractor terms with varying strengths
        attractor_terms = 0.0
        for i in range(4):
            dist = 0.0
            for j in range(self.dim):
                dist += (x[j] - self.attractor_centers[i, j])**2
            attractor_terms += self.attractor_strengths[i] * np.exp(-0.5 * dist)
        
        # Compute cross-dimensional coupling terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Compute harmonic interaction terms
        harmonic_terms = 0.0
        for j in range(self.dim):
            harmonic_terms += self.harmonic_coeffs[j] * np.sin(2.0 * x[j]) * np.cos(x[j])
        
        # Combine all components with appropriate weights
        total = 1.2 * sin_terms + 0.8 * rbf_terms + 0.6 * cond_terms + 0.4 * attractor_terms + 0.3 * coupling_terms + 0.2 * harmonic_terms
        
        # Add a novel component: multi-scale chaotic modulation with exponential decay (enhanced)
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += (np.sin(5.0 * x[j]) * np.cos(3.0 * x[j]) + 
                               0.7 * np.sin(7.0 * x[j]) * np.cos(2.0 * x[j])) * np.exp(-0.15 * np.abs(x[j]))
        
        # Add another novel component: polynomial-hyperbolic hybrid with dynamic exponents
        poly_hybrid = 0.0
        for j in range(self.dim):
            poly_hybrid += (x[j]**3) * np.tanh(0.5 * x[j]) + 0.7 * np.sinh(x[j]) + 0.3 * np.log(1.0 + np.abs(x[j]))
        
        # Final combination with refined weights
        total = 1.3 * sin_terms + 0.9 * rbf_terms + 0.7 * cond_terms + 0.5 * attractor_terms + 0.4 * coupling_terms + 0.3 * harmonic_terms + 0.3 * chaos_modulation + 0.2 * poly_hybrid
        
        # Add enhanced hyperbolic tangent interactions
        tanh_interaction = 0.0
        for j in range(self.dim):
            tanh_interaction += 0.4 * np.tanh(2.0 * x[j]) * np.sin(0.5 * x[j])
            
        total += 0.15 * tanh_interaction
        
        return total
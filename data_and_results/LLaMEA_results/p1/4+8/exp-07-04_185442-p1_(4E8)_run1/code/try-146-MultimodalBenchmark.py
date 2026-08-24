import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r_constants = np.linspace(3.5, 4.2, dim)
        self.sigma = 0.02
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-cosine map with time-varying parameters
        chaotic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            chaotic_terms[i] = r * np.sin(x_i) * np.cos(x_i) * np.exp(-0.5 * x_i**2)
        
        # Modified multiquadratic RBF with dynamic centers and variable conditioning
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma * (i + 1)**1.5
        
        # Adaptive gradient modulation with multiple harmonic components
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            grad_mod[i] = (np.exp(-0.2 * x_norm[i]**2) * 
                          np.cos(2 * x_norm[i]) * 
                          np.sin(3 * x_norm[i]) * 
                          np.tan(0.5 * x_norm[i]))
        
        # Additional nonlinear cross-terms with dynamic coupling coefficients
        cross_terms = np.zeros(self.dim)
        for i in range(self.dim):
            j = (i + 2) % self.dim
            cross_terms[i] = (x_norm[i]**2) * (x_norm[j]**3) * np.sin(5 * x_norm[i] * x_norm[j])
        
        # Combine all terms with improved separability and coupling
        term1 = np.sum(chaotic_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.sin(6 * x_norm))
        term4 = np.sum(np.cos(4 * x_norm) * np.exp(-0.2 * x_norm**2))
        term5 = 0.5 * np.sum((x_norm[0] * x_norm[1])**4)
        
        # Enhanced dynamic coupling between dimensions with nonlinear interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**4 * np.sin(x_norm[i] * x_norm[i+1] * 2)
        
        # Add higher-order polynomial noise with dynamic scaling
        noise = 0.01 * np.random.random() * np.sum(x_norm**5)
        
        # Add a global periodic modulation to increase landscape irregularity
        periodic_mod = np.sin(0.3 * np.sum(x_norm**2)) * np.cos(0.7 * np.sum(x_norm))
        
        return term1 + term2 + term3 + term4 + term5 + coupling + noise + periodic_mod
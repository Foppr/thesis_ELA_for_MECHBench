import numpy as np

class ChaoticSphericalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters with enhanced complexity
        self.tent_r = np.random.uniform(2.8, 3.9, size=dim)
        # Spherical harmonics coefficients with higher degree terms
        self.sph_l = np.random.randint(1, 8, size=dim)
        self.sph_m = np.random.randint(-7, 8, size=dim)
        # Quantum interference parameters with phase modulation
        self.q_amp = np.random.uniform(0.8, 2.5, size=dim)
        self.q_phase = np.random.uniform(0, 4*np.pi, size=dim)
        self.q_freq = np.random.uniform(2.0, 8.0, size=dim)
        # Fractal scaling factors with exponential components
        self.fractal_scale = np.random.uniform(0.05, 1.5, size=dim)
        # Enhanced coupling coefficients for stronger non-linear interactions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        # Adaptive basin centers with dynamic scaling
        self.basin_centers = np.random.uniform(-4.5, 4.5, size=dim)
        # Additional chaotic parameter for enhanced complexity
        self.tent_a = np.random.uniform(0.1, 0.9, size=dim)
        # Multi-scale harmonic components
        self.harmonic_freq = np.random.uniform(0.5, 3.0, size=dim)
        # Adaptive penalty weights
        self.penalty_weights = np.random.uniform(0.3, 1.2, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced tent map chaotic component with multiple iterations
        tent_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple chaotic iterations for enhanced complexity
            for _ in range(3):
                if xi < 0.5:
                    xi = self.tent_r[i] * xi
                else:
                    xi = self.tent_r[i] * (1 - xi)
            tent_component += xi
            
        # Enhanced spherical harmonics component with multi-scale terms
        sph_component = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            if r > 1e-8:
                theta = np.arccos(x[i] / r)
                phi = np.arctan2(x[(i+1)%self.dim], x[i])
                # Multi-scale spherical harmonics
                sph_val = (self.sph_l[i]**2) * np.cos(self.sph_m[i] * phi) * np.sin(theta)**self.sph_l[i]
                sph_component += sph_val
                
        # Enhanced quantum interference component with amplitude modulation
        q_component = 0.0
        for i in range(self.dim):
            # Quantum interference with multiple frequencies
            q_val = self.q_amp[i] * np.sin(self.q_freq[i] * x[i] + self.q_phase[i]) * \
                   np.cos(self.harmonic_freq[i] * x[i])
            q_component += q_val
            
        # Enhanced fractal scaling component with exponential terms
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_val = self.fractal_scale[i] * (x[i]**5 + x[i]**4 + x[i]**3)
            fractal_component += fractal_val
            
        # Enhanced non-linear coupling component with cross-dimensional interactions
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Enhanced coupling with trigonometric functions and additional polynomial terms
                    coupling_component += self.coupling_matrix[i, j] * x[i] * np.sin(x[j]) * \
                                        np.cos(x[i] + x[j]) * (x[i]**2 + x[j]**2)
                    
        # Adaptive basin attraction component
        basin_component = 0.0
        for i in range(self.dim):
            # Adaptive basin with penalty weights and modified quadratic term
            basin_val = self.penalty_weights[i] * (x[i] - self.basin_centers[i])**3
            basin_component += basin_val
            
        # Additional chaotic cross-dimensional interaction terms
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional chaotic interaction with modified exponential decay
                cross_val = np.sin(x[i] * x[j]) * np.exp(-0.5*abs(x[i] - x[j]))
                cross_component += cross_val
                
        # Combine all components with adjusted weights for better balance
        return (1.3 * tent_component + 
                1.4 * sph_component + 
                1.2 * q_component + 
                1.0 * fractal_component + 
                0.9 * coupling_component + 
                0.8 * basin_component + 
                0.7 * cross_component)
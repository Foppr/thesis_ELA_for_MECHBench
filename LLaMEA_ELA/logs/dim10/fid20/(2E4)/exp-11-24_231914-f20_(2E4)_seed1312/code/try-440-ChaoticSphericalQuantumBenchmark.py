import numpy as np

class ChaoticSphericalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.tent_r = np.random.uniform(1.5, 3.9, size=dim)
        # Spherical harmonics coefficients
        self.sph_l = np.random.randint(0, 5, size=dim)
        self.sph_m = np.random.randint(-5, 6, size=dim)
        # Quantum interference parameters
        self.q_amp = np.random.uniform(0.5, 2.0, size=dim)
        self.q_phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.q_freq = np.random.uniform(1.0, 5.0, size=dim)
        # Fractal scaling factors
        self.fractal_scale = np.random.uniform(0.1, 1.0, size=dim)
        # Coupling coefficients for non-linear interactions
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, size=(dim, dim))
        # Basin of attraction centers
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi < 0.5:
                tent_val = self.tent_r[i] * xi
            else:
                tent_val = self.tent_r[i] * (1 - xi)
            tent_component += tent_val
            
        # Spherical harmonics component
        sph_component = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            if r > 1e-8:
                theta = np.arccos(x[i] / r)
                phi = np.arctan2(x[(i+1)%self.dim], x[i])
                sph_val = self.sph_l[i] * np.cos(self.sph_m[i] * phi) * np.sin(theta)**self.sph_l[i]
                sph_component += sph_val
                
        # Quantum interference component
        q_component = 0.0
        for i in range(self.dim):
            q_val = self.q_amp[i] * np.sin(self.q_freq[i] * x[i] + self.q_phase[i])
            q_component += q_val
            
        # Fractal scaling component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_val = self.fractal_scale[i] * (x[i]**3 + x[i]**2)
            fractal_component += fractal_val
            
        # Non-linear coupling component
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * np.sin(x[j])
                    
        # Basin attraction component
        basin_component = 0.0
        for i in range(self.dim):
            basin_val = (x[i] - self.basin_centers[i])**2
            basin_component += basin_val
            
        # Combine all components with appropriate weights
        return (1.3 * tent_component + 
                1.1 * sph_component + 
                0.9 * q_component + 
                0.7 * fractal_component + 
                0.6 * coupling_component + 
                0.5 * basin_component)
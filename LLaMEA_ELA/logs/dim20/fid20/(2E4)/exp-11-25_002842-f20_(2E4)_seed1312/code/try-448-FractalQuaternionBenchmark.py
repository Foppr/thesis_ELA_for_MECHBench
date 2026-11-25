import numpy as np

class FractalQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers with fractal distribution
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 20))
        # Fractal noise parameters for terrain generation
        self.fractal_params = np.random.uniform(0.1, 2.0, dim)
        # Quaternion coupling coefficients for high-dimensional interactions
        self.quat_coupling = np.random.uniform(-1.0, 1.0, (dim, dim, dim))
        # Temporal chaos parameters with time-varying behavior
        self.temporal_params = np.random.uniform(0.01, 0.5, dim)
        # Multi-scale Gaussian components for multimodality
        self.gauss_means = np.random.uniform(-5.0, 5.0, (dim, 15))
        self.gauss_vars = np.random.uniform(0.2, 3.0, (dim, 15))
        self.gauss_weights = np.random.dirichlet(np.ones(15), dim)
        # Adaptive conditioning with fractal scaling
        self.conditioning_factors = np.random.uniform(0.5, 3.0, dim)
        # Coupling strength between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 2.0, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial basis function components
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(20):
                dist = np.sum((x - self.rbf_centers[i, j])**2)
                rbf_sum += np.exp(-dist / (2 * self.fractal_params[i]**2))
            rbf_energy += rbf_sum
            
        # Fractal noise component with multi-scale roughness
        fractal_energy = 0.0
        for i in range(self.dim):
            noise = 0.0
            scale = 1.0
            for _ in range(5):
                noise += scale * np.sin(x[i] * scale)
                scale *= 2
            fractal_energy += noise
            
        # Quaternion-based coupling between dimensions
        quat_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    for k in range(self.dim):
                        quat_energy += self.quat_coupling[i, j, k] * np.sin(x[i]) * np.cos(x[j]) * np.tan(x[k])
                        
        # Temporal chaos component with delayed feedback
        temporal_energy = 0.0
        for i in range(self.dim):
            temporal_energy += self.temporal_params[i] * np.sin(x[i] * (1 + 0.1 * np.sin(x[(i+1)%self.dim])))
            
        # Multi-scale Gaussian mixture components
        gauss_energy = 0.0
        for i in range(self.dim):
            gauss_sum = 0.0
            for k in range(15):
                gauss_sum += self.gauss_weights[i, k] * np.exp(-0.5 * ((x[i] - self.gauss_means[i, k]) ** 2) / (self.gauss_vars[i, k] ** 2))
            gauss_energy += -np.log(gauss_sum)
            
        # Adaptive conditioning with fractal scaling
        cond_energy = 0.0
        for i in range(self.dim):
            cond_energy += self.conditioning_factors[i] * (x[i] ** 4) * np.cos(x[i])
            
        # Coupling between dimensions with varying strengths
        coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_energy += self.coupling_strengths[i, j] * np.sin(x[i] * x[j])
        
        # Combine all components with appropriate weights
        total = 0.25 * rbf_energy + 0.15 * fractal_energy + 0.12 * quat_energy + 0.10 * temporal_energy + 0.15 * gauss_energy + 0.10 * cond_energy + 0.13 * coupling_energy
        
        return total
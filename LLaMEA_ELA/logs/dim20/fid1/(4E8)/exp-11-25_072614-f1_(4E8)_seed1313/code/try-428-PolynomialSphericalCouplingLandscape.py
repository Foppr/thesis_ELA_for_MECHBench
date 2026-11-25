import numpy as np

class PolynomialSphericalCouplingLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial conditioning parameters
        self.poly_degree = 3 + np.random.randint(0, 3)
        self.conditioning_strength = 0.5 + 1.5 * np.random.rand()
        # Spherical harmonics parameters
        self.sphere_harmonics_amplitude = 0.5 + 2.0 * np.random.rand()
        self.sphere_harmonics_frequency = 1.0 + 3.0 * np.random.rand()
        # Quaternion coupling parameters
        self.rotation_strength = 0.3 + 1.2 * np.random.rand()
        self.quaternion_phase = np.pi * np.random.rand()
        # Local minima distribution
        self.minima_count = 5 + np.random.randint(0, 5)
        self.minima_spread = 1.0 + 2.0 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial conditioning component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**self.poly_degree) * (1.0 + self.conditioning_strength * np.sin(0.5 * x[i]))
        
        # Spherical harmonics component
        sphere_term = 0.0
        # Normalize vector for spherical coordinates
        r = np.linalg.norm(x)
        if r > 1e-8:
            theta = np.arccos(x[0] / r) if self.dim > 0 else 0.0
            phi = np.arctan2(x[1], x[0]) if self.dim > 1 else 0.0
            
            sphere_term = self.sphere_harmonics_amplitude * np.sin(self.sphere_harmonics_frequency * theta) * np.cos(self.sphere_harmonics_frequency * phi)
        
        # Quaternion-based rotational coupling
        quat_term = 0.0
        if self.dim >= 4:
            # Simple quaternion-like interaction between first four dimensions
            q_real = x[0]
            q_imag = np.array([x[1], x[2], x[3]])
            # Compute dot product with phase-shifted vector
            phase_vec = np.array([np.cos(self.quaternion_phase), np.sin(self.quaternion_phase), 0.0, 0.0])
            quat_term = self.rotation_strength * (q_real * phase_vec[0] + np.dot(q_imag, phase_vec[1:]))
        
        # Multi-local minima attraction
        minima_term = 0.0
        for i in range(self.minima_count):
            center = np.array([5.0 * np.sin(i * np.pi / self.minima_count), 
                              5.0 * np.cos(i * np.pi / self.minima_count)] + [0.0] * (self.dim - 2))
            dist = np.linalg.norm(x - center)
            minima_term += np.exp(-0.5 * (dist / self.minima_spread)**2)
        
        # Combine all components with appropriate weights
        result = poly_term + sphere_term + quat_term - minima_term
        
        return result
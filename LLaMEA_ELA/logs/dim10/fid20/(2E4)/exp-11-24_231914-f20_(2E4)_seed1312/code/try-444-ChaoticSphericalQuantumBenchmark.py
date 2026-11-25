import numpy as np

class ChaoticSphericalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters
        self.chebyshev_coeffs = np.random.uniform(-1.0, 1.0, size=dim)
        # Spherical harmonics coefficients
        self.sphere_degree = np.random.randint(1, 5, size=dim)
        self.sphere_order = np.random.randint(-3, 4, size=dim)
        # Quantum-like interference terms
        self.quantum_amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        # Fractal scaling factors
        self.fractal_scaling = np.random.uniform(0.1, 2.0, size=dim)
        # Cross-dimensional coupling with chaotic interactions
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, size=(dim, dim))
        # Non-linear transformation parameters
        self.nonlinear_exponents = np.random.uniform(1.5, 4.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        chaotic_component = 0.0
        for i in range(self.dim):
            # Tent map: f(x) = r * min(x, 1-x) where r=2 (chaotic behavior)
            tent_val = 2.0 * np.minimum(x[i], 1.0 - x[i])
            chaotic_component += self.chebyshev_coeffs[i] * tent_val
            
        # Spherical harmonics component
        sphere_component = 0.0
        for i in range(self.dim):
            # Use Chebyshev polynomials as approximation to spherical harmonics
            theta = np.arccos(x[i] / (1e-8 + np.linalg.norm(x))) if np.linalg.norm(x) > 1e-8 else 0.0
            sphere_val = np.cos(self.sphere_degree[i] * theta + self.sphere_order[i])
            sphere_component += sphere_val
            
        # Quantum-like interference component
        quantum_component = 0.0
        for i in range(self.dim):
            # Interference pattern from quantum harmonic oscillator
            quantum_val = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] + x[i])
            quantum_component += quantum_val
            
        # Fractal scaling component
        fractal_component = 0.0
        for i in range(self.dim):
            # Apply fractal-like scaling with non-linear transformation
            fractal_val = self.fractal_scaling[i] * np.power(np.abs(x[i]), self.nonlinear_exponents[i])
            fractal_component += fractal_val
            
        # Cross-dimensional coupling with chaotic interaction
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * np.sin(x[i] + x[j])
                    
        # Combine all components with appropriate weights
        return (1.2 * chaotic_component + 
                1.5 * sphere_component + 
                1.0 * quantum_component + 
                0.8 * fractal_component + 
                0.6 * coupling_component)
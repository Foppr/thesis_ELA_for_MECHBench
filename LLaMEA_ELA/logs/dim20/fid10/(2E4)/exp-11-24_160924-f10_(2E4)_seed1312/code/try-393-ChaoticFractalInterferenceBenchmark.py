import numpy as np

class ChaoticFractalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Enhanced chaotic system parameters with wider ranges
        self.chebyshev_coeffs = np.random.uniform(-2.0, 2.0, (dim, 4))
        self.logistic_r = np.random.uniform(3.5, 4.2, dim)
        self.henon_a = np.random.uniform(1.2, 1.6, dim)
        self.henon_b = np.random.uniform(0.1, 0.4, dim)
        # Increased fractal complexity with multiple scaling factors
        self.fractal_dims = np.random.uniform(1.0, 3.5, dim)
        self.fractal_scaling = np.random.uniform(0.02, 1.0, dim)
        # Quantum interference with multi-level phase coupling
        self.quantum_phases = np.random.uniform(0, 4*np.pi, (dim, dim))
        self.quantum_amplitudes = np.random.uniform(0.5, 3.0, (dim, dim))
        # Additional discontinuity and noise parameters
        self.discontinuity_points = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.noise_level = np.random.uniform(0.01, 0.2, dim)
        # New high-order polynomial coupling terms
        self.poly_coupling = np.random.uniform(-0.5, 0.5, (dim, 5))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced chaotic dynamical systems with higher iterations
        for i in range(self.dim):
            # Extended Chebyshev polynomial chaos
            cheb_val = (self.chebyshev_coeffs[i][0] + 
                       self.chebyshev_coeffs[i][1] * x[i] + 
                       self.chebyshev_coeffs[i][2] * (2 * x[i]**2 - 1) +
                       self.chebyshev_coeffs[i][3] * (4 * x[i]**3 - 3 * x[i]))
            result += np.abs(cheb_val)
            
            # Logistic map with more iterations
            logistic_val = x[i]
            for _ in range(12):
                logistic_val = self.logistic_r[i] * logistic_val * (1 - logistic_val)
            result += np.abs(logistic_val)
            
            # Hénon map with more iterations
            henon_x, henon_y = x[i], 0.0
            for _ in range(8):
                new_x = 1 - self.henon_a[i] * henon_x**2 + henon_y
                new_y = self.henon_b[i] * henon_x
                henon_x, henon_y = new_x, new_y
            result += np.abs(henon_x)
            
        # Complex fractal-like structure with multiple iterations
        for i in range(self.dim):
            fractal_term = 0.0
            for j in range(10):
                point = self.discontinuity_points[i][j]
                distance = np.abs(x[i] - point)
                fractal_term += (distance ** self.fractal_dims[i]) * self.fractal_scaling[i]
            result += fractal_term
            
        # Multi-level quantum interference patterns
        for i in range(self.dim):
            quantum_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_diff = self.quantum_phases[i][j]
                    amplitude = self.quantum_amplitudes[i][j]
                    quantum_sum += amplitude * np.sin(x[i] * x[j] + phase_diff)
            result += 0.8 * quantum_sum**3
            
        # Enhanced discontinuous noise terms
        for i in range(self.dim):
            noise_term = 0.0
            for j in range(7):
                if np.abs(x[i] - self.discontinuity_points[i][j]) < 0.2:
                    noise_term += self.noise_level[i] * np.random.uniform(-1, 1) * np.sin(20 * x[i])
            result += noise_term
            
        # High-frequency oscillation with multiple components
        for i in range(self.dim):
            result += 4.0 * np.sin(15 * x[i]) * np.cos(11 * x[i]) + 2.0 * np.sin(7 * x[i])**2
            
        # Advanced cross-dimensional coupling with polynomial terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] - x[j])**5 + 0.5 * (x[i]**2 - x[j]**2)**3
        result += 0.7 * cross_term
        
        # New high-order polynomial coupling terms
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(5):
                if j < self.dim:
                    poly_term += self.poly_coupling[i][j] * x[i]**(j+2) * x[j%self.dim]**2
        result += 0.3 * poly_term
        
        # Global scaling with higher-order terms
        result *= (1.0 + 0.6 * np.sum(np.abs(x)) + 0.1 * np.sum(x**4))
        
        return result
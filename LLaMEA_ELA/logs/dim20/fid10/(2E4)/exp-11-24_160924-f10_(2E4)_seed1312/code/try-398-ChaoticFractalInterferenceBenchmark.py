import numpy as np

class ChaoticFractalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic system parameters with modified ranges
        self.chebyshev_coeffs = np.random.uniform(-2.0, 2.0, (dim, 4))
        self.logistic_r = np.random.uniform(3.5, 4.2, dim)
        self.henon_a = np.random.uniform(1.2, 1.6, dim)
        self.henon_b = np.random.uniform(0.1, 0.4, dim)
        # Fractal structure parameters with increased complexity
        self.fractal_dims = np.random.uniform(1.0, 3.5, dim)
        self.fractal_scaling = np.random.uniform(0.02, 1.0, dim)
        # Quantum interference parameters with stronger coupling
        self.quantum_phases = np.random.uniform(0, 4*np.pi, (dim, dim))
        self.quantum_amplitudes = np.random.uniform(0.5, 3.0, (dim, dim))
        # Discontinuity and noise parameters with higher variability
        self.discontinuity_points = np.random.uniform(-5.0, 5.0, (dim, 9))
        self.noise_level = np.random.uniform(0.01, 0.2, dim)
        # Additional high-order polynomial terms for increased complexity
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (dim, 5))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic dynamical systems (Chebyshev polynomials and logistic maps)
        for i in range(self.dim):
            # Extended Chebyshev polynomial chaos
            cheb_val = (self.chebyshev_coeffs[i][0] + 
                       self.chebyshev_coeffs[i][1] * x[i] + 
                       self.chebyshev_coeffs[i][2] * (2 * x[i]**2 - 1) +
                       self.chebyshev_coeffs[i][3] * (4 * x[i]**3 - 3 * x[i]))
            result += np.abs(cheb_val)
            
            # Logistic map chaos with higher iteration count
            logistic_val = x[i]
            for _ in range(10):
                logistic_val = self.logistic_r[i] * logistic_val * (1 - logistic_val)
            result += np.abs(logistic_val)
            
            # Hénon map chaos with additional iterations
            henon_x, henon_y = x[i], 0.0
            for _ in range(8):
                new_x = 1 - self.henon_a[i] * henon_x**2 + henon_y
                new_y = self.henon_b[i] * henon_x
                henon_x, henon_y = new_x, new_y
            result += np.abs(henon_x)
            
        # Fractal-like geometric structure with more complex terms
        for i in range(self.dim):
            fractal_term = 0.0
            for j in range(9):
                point = self.discontinuity_points[i][j]
                distance = np.abs(x[i] - point)
                fractal_term += (distance ** self.fractal_dims[i]) * self.fractal_scaling[i]
            result += fractal_term
            
        # Quantum interference patterns with additional cross-dimensional terms
        for i in range(self.dim):
            quantum_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_diff = self.quantum_phases[i][j]
                    amplitude = self.quantum_amplitudes[i][j]
                    quantum_sum += amplitude * np.sin(x[i] * x[j] + phase_diff) * np.cos(x[i] + x[j])
            result += 0.8 * quantum_sum**2
            
        # Add discontinuous noise terms with higher frequency and more points
        for i in range(self.dim):
            noise_term = 0.0
            for j in range(7):
                if np.abs(x[i] - self.discontinuity_points[i][j]) < 0.1:
                    noise_term += self.noise_level[i] * np.random.uniform(-1, 1) * np.sin(20 * x[i])
            result += noise_term
            
        # Add high-frequency oscillation to increase complexity
        for i in range(self.dim):
            result += 4.0 * np.sin(15 * x[i]) * np.cos(11 * x[i]) + 2.0 * np.sin(7 * x[i]**2)
            
        # Add cross-dimensional coupling terms for increased difficulty with higher order
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] - x[j])**5 + 0.5 * (x[i] + x[j])**3
        result += 0.6 * cross_term
        
        # Add high-order polynomial terms
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(5):
                poly_term += self.poly_coeffs[i][j] * (x[i]**(j+1))
            result += 0.3 * poly_term
            
        # Add a global scaling factor to control overall difficulty
        result *= (1.0 + 0.6 * np.sum(np.abs(x)) + 0.2 * np.sum(x**4))
        
        return result
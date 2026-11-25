import numpy as np

class QuaternionRotationalFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quaternion-based rotational parameters
        self.rotation_matrices = []
        for i in range(dim // 2 + 1):
            angle = np.random.uniform(0, 2 * np.pi)
            axis = np.random.randn(3)
            axis = axis / np.linalg.norm(axis)
            # Generate rotation matrix using Rodrigues' rotation formula
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            I = np.eye(3)
            K = np.array([[0, -axis[2], axis[1]],
                          [axis[2], 0, -axis[0]],
                          [-axis[1], axis[0], 0]])
            R = I + sin_a * K + (1 - cos_a) * np.dot(K, K)
            self.rotation_matrices.append(R)
        
        # Fractal-like conditioning parameters
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        self.fractal_exponents = np.random.uniform(0.3, 1.7, dim)
        
        # Memory-enhanced cosine modulations
        self.cosine_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.memory_coefficients = np.random.uniform(0.1, 0.6, dim)
        
        # Multi-modal Gaussian components
        self.gaussian_centers = np.random.uniform(-4, 4, (dim, 2))
        self.gaussian_heights = np.random.uniform(0.5, 3.0, (dim, 2))
        self.gaussian_widths = np.random.uniform(0.2, 1.8, (dim, 2))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-based rotational couplings
        rotational_coupling = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                # Pairwise rotation
                pair = x[i:i+2]
                R = self.rotation_matrices[i // 2 % len(self.rotation_matrices)]
                rotated_pair = np.dot(R, pair)
                rotational_coupling += np.sum(rotated_pair**2) * (1.0 + 0.3 * np.sin(0.5 * x[i]))
        
        # Fractal-like conditioning with adaptive scaling
        fractal_conditioning = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i]
            fractal_exp = self.fractal_exponents[i]
            fractal_term = np.abs(x[i])**fractal_exp
            fractal_conditioning += cond_factor * fractal_term
        
        # Memory-enhanced cosine modulations
        memory_cosine = 0.0
        for i in range(self.dim):
            freq = self.cosine_frequencies[i]
            mem_coeff = self.memory_coefficients[i]
            if i > 0:
                memory_effect = mem_coeff * np.cos(0.3 * x[i-1])
            else:
                memory_effect = 0.0
            memory_cosine += (np.cos(freq * x[i]) + memory_effect) * np.exp(-0.1 * abs(x[i]))
        
        # Multi-modal Gaussian peaks
        gaussian_sum = 0.0
        for i in range(self.dim):
            for j in range(2):
                center = self.gaussian_centers[i, j]
                height = self.gaussian_heights[i, j]
                width = self.gaussian_widths[i, j]
                gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional hyperbolic coupling
        hyperbolic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                diff = x[i] - x[j]
                hyperbolic_coupling += np.tanh(diff) * np.exp(-0.2 * abs(diff))
        
        # Combined function with dimensionally varying weights
        dim_factor = 1.0 + 0.1 * np.log(self.dim)
        return (0.25 * gaussian_sum + 0.20 * rotational_coupling +
                0.20 * fractal_conditioning + 0.15 * memory_cosine +
                0.10 * hyperbolic_coupling) * dim_factor